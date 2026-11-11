#!/usr/bin/env python3
"""Build the Python library notebook with LuaLaTeX."""

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

ROOT = Path(__file__).resolve().parents[1]


def escape(text):
    replacements = {
        "\\": r"\textbackslash{}",
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
        "{": r"\{",
        "}": r"\}",
        "~": r"\textasciitilde{}",
        "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(c, c) for c in text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", type=Path, default=ROOT / "algorithm_library/python/notebook.pdf"
    )
    parser.add_argument("--force", action="store_true", help="rebuild even if unchanged")
    parser.add_argument("--stage", action="store_true", help="stage the PDF for commit")
    args = parser.parse_args()
    output = args.output.resolve()
    source = ROOT / "algorithm_library/python"
    exclude_file = ROOT / "tools/notebook-exclude.txt"
    excluded = {
        line.strip()
        for line in exclude_file.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.lstrip().startswith("#")
    }

    def file_order(path):
        relative = path.relative_to(source)
        priority = (
            0
            if relative.parent == Path(".")
            else 1
            if relative.parts[0] == "gen"
            else 2
        )
        return priority, relative.as_posix()

    files = sorted(
        (
            path
            for path in source.rglob("*.py")
            if path.relative_to(source).as_posix() not in excluded
            and path.relative_to(ROOT).as_posix() not in excluded
        ),
        key=file_order,
    )
    if not files:
        parser.error(f"No Python files found in {source}")

    # Check contents rather than mtimes: pre-commit temporarily restores files.
    digest = hashlib.sha256()
    for path in [Path(__file__).resolve(), exclude_file, *files]:
        digest.update(path.relative_to(ROOT).as_posix().encode())
        digest.update(b"\0")
        digest.update(path.read_bytes())
        digest.update(b"\0")
    source_hash = digest.hexdigest()
    cache_key = hashlib.sha256(str(output).encode()).hexdigest()
    cache_path = ROOT / "build/notebook" / f"{cache_key}.json"
    try:
        cache = json.loads(cache_path.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        cache = {}
    if (
        not args.force
        and isinstance(cache, dict)
        and cache.get("source") == source_hash
        and output.is_file()
        and cache.get("pdf") == hashlib.sha256(output.read_bytes()).hexdigest()
    ):
        if args.stage:
            subprocess.run(["git", "-C", str(ROOT), "add", "--", str(output)], check=True)
        print(f"Up to date: {output}")
        return

    if not shutil.which("lualatex"):
        parser.error("lualatex is required (see README.md)")
    from pygments import highlight
    from pygments.formatters import LatexFormatter
    from pygments.lexers import PythonLexer

    # Suppress volatile PDF metadata, including the trailer ID derived from
    # the randomly named temporary build directory.
    preamble = r"""\pdfvariable suppressoptionalinfo 767\relax
\documentclass[a4paper,9pt,twocolumn]{extarticle}
\usepackage[margin=10mm,top=15mm,bottom=15mm]{geometry}
\usepackage{luatexja-fontspec}
\setmainjfont{IPAexGothic}
\setsansjfont{IPAexGothic}
\setmonojfont{IPAexGothic}
\usepackage{fvextra}
\usepackage{xcolor}
\usepackage{fancyhdr}
\usepackage[hidelinks,unicode]{hyperref}
\pagestyle{fancy}
\fancyhf{}
\fancyhead[L]{Python Algorithm Library}
\fancyhead[R]{\thepage}
\setlength{\headheight}{12pt}
\setlength{\columnsep}{7mm}
\setcounter{tocdepth}{2}
\begin{document}
\pdfbookmark[0]{Python Algorithm Library}{title}
\section*{Python Algorithm Library}
\tableofcontents
\clearpage
"""
    with tempfile.TemporaryDirectory(prefix="python-notebook-") as directory:
        work = Path(directory)
        formatter = LatexFormatter(
            style="friendly",
            verboptions=r"fontsize=\fontsize{8}{8}\selectfont,numbers=left,numbersep=3pt,breaklines=true,breakanywhere=true,tabsize=4",
        )
        parts = [
            preamble.replace(
                r"\begin{document}",
                formatter.get_style_defs() + "\n" + r"\begin{document}",
            )
        ]
        category = None
        for path in files:
            relative = path.relative_to(source)
            group = relative.parent.as_posix()
            if group != category:
                category = group
                parts.append(
                    r"\section{"
                    + escape(group if group != "." else "Templates")
                    + "}\n"
                )
            parts.append(r"\subsection{" + escape(path.name) + "}\n")
            # Pygments escapes TeX characters; source code is never executed.
            parts.append(
                highlight(path.read_text(encoding="utf-8"), PythonLexer(), formatter)
            )
        parts.append(r"\end{document}")
        (work / "notebook.tex").write_text("".join(parts), encoding="utf-8")
        # Two passes resolve the table of contents and PDF links.
        for _ in range(2):
            result = subprocess.run(
                [
                    "lualatex",
                    "-interaction=nonstopmode",
                    "-halt-on-error",
                    "notebook.tex",
                ],
                cwd=work,
                stdout=subprocess.PIPE,
                stderr=subprocess.STDOUT,
                text=True,
                env={**os.environ, "SOURCE_DATE_EPOCH": "0", "FORCE_SOURCE_DATE": "1"},
            )
            if result.returncode:
                raise SystemExit(result.stdout)
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(work / "notebook.pdf", output)
    cache_path.parent.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(
        json.dumps({"source": source_hash, "pdf": hashlib.sha256(output.read_bytes()).hexdigest()}),
        encoding="utf-8",
    )
    if args.stage:
        subprocess.run(["git", "-C", str(ROOT), "add", "--", str(output)], check=True)
    print(f"Created {output} ({len(files)} files)")


if __name__ == "__main__":
    main()
