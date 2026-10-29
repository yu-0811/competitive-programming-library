#!/usr/bin/env python3
"""Build the Python library notebook with LuaLaTeX."""

import argparse
import os
from pathlib import Path
import shutil
import subprocess
import tempfile

from pygments import highlight
from pygments.formatters import LatexFormatter
from pygments.lexers import PythonLexer


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
    args = parser.parse_args()
    if not shutil.which("lualatex"):
        parser.error("lualatex is required (see README.md)")
    source = ROOT / "algorithm_library/python"

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
        (path for path in source.rglob("*.py") if path != source / "template.py"),
        key=file_order,
    )
    if not files:
        parser.error(f"No Python files found in {source}")
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
            verboptions=r"fontsize=\fontsize{6}{7}\selectfont,numbers=left,numbersep=3pt,breaklines=true,breakanywhere=true,tabsize=4",
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
        output = args.output.resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        shutil.copyfile(work / "notebook.pdf", output)
    print(f"Created {output} ({len(files)} files)")


if __name__ == "__main__":
    main()
