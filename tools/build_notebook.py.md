---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links: []
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \                  ^^^^^^\n  File \"/opt/hostedtoolcache/PyPy/3.11.17/x64/lib/pypy3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "#!/usr/bin/env python3\n\"\"\"Build the Python library notebook with LuaLaTeX.\"\
    \"\"\n\nimport argparse\nimport os\nfrom pathlib import Path\nimport shutil\n\
    import subprocess\nimport tempfile\n\nfrom pygments import highlight\nfrom pygments.formatters\
    \ import LatexFormatter\nfrom pygments.lexers import PythonLexer\n\n\nROOT = Path(__file__).resolve().parents[1]\n\
    \n\ndef escape(text):\n    replacements = {\n        \"\\\\\": r\"\\textbackslash{}\"\
    ,\n        \"&\": r\"\\&\",\n        \"%\": r\"\\%\",\n        \"$\": r\"\\$\"\
    ,\n        \"#\": r\"\\#\",\n        \"_\": r\"\\_\",\n        \"{\": r\"\\{\"\
    ,\n        \"}\": r\"\\}\",\n        \"~\": r\"\\textasciitilde{}\",\n       \
    \ \"^\": r\"\\textasciicircum{}\",\n    }\n    return \"\".join(replacements.get(c,\
    \ c) for c in text)\n\n\ndef main():\n    parser = argparse.ArgumentParser(description=__doc__)\n\
    \    parser.add_argument(\n        \"--output\", type=Path, default=ROOT / \"\
    algorithm_library/python/notebook.pdf\"\n    )\n    args = parser.parse_args()\n\
    \    if not shutil.which(\"lualatex\"):\n        parser.error(\"lualatex is required\
    \ (see README.md)\")\n    source = ROOT / \"algorithm_library/python\"\n    exclude_file\
    \ = ROOT / \"tools/notebook-exclude.txt\"\n    excluded = {\n        line.strip()\n\
    \        for line in exclude_file.read_text(encoding=\"utf-8\").splitlines()\n\
    \        if line.strip() and not line.lstrip().startswith(\"#\")\n    }\n\n  \
    \  def file_order(path):\n        relative = path.relative_to(source)\n      \
    \  priority = (\n            0\n            if relative.parent == Path(\".\")\n\
    \            else 1\n            if relative.parts[0] == \"gen\"\n           \
    \ else 2\n        )\n        return priority, relative.as_posix()\n\n    files\
    \ = sorted(\n        (\n            path\n            for path in source.rglob(\"\
    *.py\")\n            if path.relative_to(source).as_posix() not in excluded\n\
    \            and path.relative_to(ROOT).as_posix() not in excluded\n        ),\n\
    \        key=file_order,\n    )\n    if not files:\n        parser.error(f\"No\
    \ Python files found in {source}\")\n    # Suppress volatile PDF metadata, including\
    \ the trailer ID derived from\n    # the randomly named temporary build directory.\n\
    \    preamble = r\"\"\"\\pdfvariable suppressoptionalinfo 767\\relax\n\\documentclass[a4paper,9pt,twocolumn]{extarticle}\n\
    \\usepackage[margin=10mm,top=15mm,bottom=15mm]{geometry}\n\\usepackage{luatexja-fontspec}\n\
    \\setmainjfont{IPAexGothic}\n\\setsansjfont{IPAexGothic}\n\\setmonojfont{IPAexGothic}\n\
    \\usepackage{fvextra}\n\\usepackage{xcolor}\n\\usepackage{fancyhdr}\n\\usepackage[hidelinks,unicode]{hyperref}\n\
    \\pagestyle{fancy}\n\\fancyhf{}\n\\fancyhead[L]{Python Algorithm Library}\n\\\
    fancyhead[R]{\\thepage}\n\\setlength{\\headheight}{12pt}\n\\setlength{\\columnsep}{7mm}\n\
    \\setcounter{tocdepth}{2}\n\\begin{document}\n\\pdfbookmark[0]{Python Algorithm\
    \ Library}{title}\n\\section*{Python Algorithm Library}\n\\tableofcontents\n\\\
    clearpage\n\"\"\"\n    with tempfile.TemporaryDirectory(prefix=\"python-notebook-\"\
    ) as directory:\n        work = Path(directory)\n        formatter = LatexFormatter(\n\
    \            style=\"friendly\",\n            verboptions=r\"fontsize=\\fontsize{8}{8}\\\
    selectfont,numbers=left,numbersep=3pt,breaklines=true,breakanywhere=true,tabsize=4\"\
    ,\n        )\n        parts = [\n            preamble.replace(\n             \
    \   r\"\\begin{document}\",\n                formatter.get_style_defs() + \"\\\
    n\" + r\"\\begin{document}\",\n            )\n        ]\n        category = None\n\
    \        for path in files:\n            relative = path.relative_to(source)\n\
    \            group = relative.parent.as_posix()\n            if group != category:\n\
    \                category = group\n                parts.append(\n           \
    \         r\"\\section{\"\n                    + escape(group if group != \".\"\
    \ else \"Templates\")\n                    + \"}\\n\"\n                )\n   \
    \         parts.append(r\"\\subsection{\" + escape(path.name) + \"}\\n\")\n  \
    \          # Pygments escapes TeX characters; source code is never executed.\n\
    \            parts.append(\n                highlight(path.read_text(encoding=\"\
    utf-8\"), PythonLexer(), formatter)\n            )\n        parts.append(r\"\\\
    end{document}\")\n        (work / \"notebook.tex\").write_text(\"\".join(parts),\
    \ encoding=\"utf-8\")\n        # Two passes resolve the table of contents and\
    \ PDF links.\n        for _ in range(2):\n            result = subprocess.run(\n\
    \                [\n                    \"lualatex\",\n                    \"\
    -interaction=nonstopmode\",\n                    \"-halt-on-error\",\n       \
    \             \"notebook.tex\",\n                ],\n                cwd=work,\n\
    \                stdout=subprocess.PIPE,\n                stderr=subprocess.STDOUT,\n\
    \                text=True,\n                env={**os.environ, \"SOURCE_DATE_EPOCH\"\
    : \"0\", \"FORCE_SOURCE_DATE\": \"1\"},\n            )\n            if result.returncode:\n\
    \                raise SystemExit(result.stdout)\n        output = args.output.resolve()\n\
    \        output.parent.mkdir(parents=True, exist_ok=True)\n        shutil.copyfile(work\
    \ / \"notebook.pdf\", output)\n    print(f\"Created {output} ({len(files)} files)\"\
    )\n\n\nif __name__ == \"__main__\":\n    main()\n"
  dependsOn: []
  isVerificationFile: false
  path: tools/build_notebook.py
  requiredBy: []
  timestamp: '2026-11-06 23:29:09+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tools/build_notebook.py
layout: document
redirect_from:
- /library/tools/build_notebook.py
- /library/tools/build_notebook.py.html
title: tools/build_notebook.py
---
