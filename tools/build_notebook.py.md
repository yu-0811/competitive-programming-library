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
    \"\"\n\nimport argparse\nimport ast\nimport hashlib\nimport json\nimport os\n\
    from pathlib import Path\nimport shutil\nimport subprocess\nimport tempfile\n\n\
    ROOT = Path(__file__).resolve().parents[1]\nPARTIAL_CLASSES = {\n    \"data_structure/TupleSegtree.py\"\
    : (\"TupleSegtree\", {\"__init__\", \"add\"}),\n    \"data_structure/TupleLazySegtree.py\"\
    : (\n        \"TupleLazySegtree\", {\"__init__\", \"_push\", \"apply\"}\n    ),\n\
    }\n\n\ndef notebook_code(path, relative):\n    code = path.read_text(encoding=\"\
    utf-8\")\n    if relative.as_posix() not in PARTIAL_CLASSES:\n        return code\n\
    \n    class_name, method_names = PARTIAL_CLASSES[relative.as_posix()]\n    cls\
    \ = next(\n        node for node in ast.parse(code).body\n        if isinstance(node,\
    \ ast.ClassDef) and node.name == class_name\n    )\n    lines = code.splitlines(keepends=True)\n\
    \    # Keep the instructions, Columns classes, and target class declaration.\n\
    \    parts = [\"\".join(lines[:cls.lineno]).rstrip()]\n    found = set()\n   \
    \ for method in cls.body:\n        if not isinstance(method, ast.FunctionDef)\
    \ or method.name not in method_names:\n            continue\n        start = method.lineno\
    \ - 1\n        # Include comments immediately above the selected method.\n   \
    \     while start > cls.lineno and lines[start - 1].lstrip().startswith(\"#\"\
    ):\n            start -= 1\n        parts.append(\"\".join(lines[start:method.end_lineno]).rstrip())\n\
    \        found.add(method.name)\n    if found != method_names:\n        raise\
    \ ValueError(f\"Missing notebook methods in {relative}: {method_names - found}\"\
    )\n    return \"\\n\\n\".join(parts) + \"\\n\"\n\n\ndef escape(text):\n    replacements\
    \ = {\n        \"\\\\\": r\"\\textbackslash{}\",\n        \"&\": r\"\\&\",\n \
    \       \"%\": r\"\\%\",\n        \"$\": r\"\\$\",\n        \"#\": r\"\\#\",\n\
    \        \"_\": r\"\\_\",\n        \"{\": r\"\\{\",\n        \"}\": r\"\\}\",\n\
    \        \"~\": r\"\\textasciitilde{}\",\n        \"^\": r\"\\textasciicircum{}\"\
    ,\n    }\n    return \"\".join(replacements.get(c, c) for c in text)\n\n\ndef\
    \ main():\n    parser = argparse.ArgumentParser(description=__doc__)\n    parser.add_argument(\n\
    \        \"--output\", type=Path, default=ROOT / \"algorithm_library/python/notebook.pdf\"\
    \n    )\n    parser.add_argument(\"--force\", action=\"store_true\", help=\"rebuild\
    \ even if unchanged\")\n    parser.add_argument(\"--stage\", action=\"store_true\"\
    , help=\"stage the PDF for commit\")\n    args = parser.parse_args()\n    output\
    \ = args.output.resolve()\n    source = ROOT / \"algorithm_library/python\"\n\
    \    exclude_file = ROOT / \"tools/notebook-exclude.txt\"\n    excluded = {\n\
    \        line.strip()\n        for line in exclude_file.read_text(encoding=\"\
    utf-8\").splitlines()\n        if line.strip() and not line.lstrip().startswith(\"\
    #\")\n    }\n\n    def file_order(path):\n        relative = path.relative_to(source)\n\
    \        priority = (\n            0\n            if relative.parent == Path(\"\
    .\")\n            else 1\n            if relative.parts[0] == \"gen\"\n      \
    \      else 2\n        )\n        return priority, relative.as_posix()\n\n   \
    \ files = sorted(\n        (\n            path\n            for path in source.rglob(\"\
    *.py\")\n            if path.relative_to(source).as_posix() not in excluded\n\
    \            and path.relative_to(ROOT).as_posix() not in excluded\n        ),\n\
    \        key=file_order,\n    )\n    if not files:\n        parser.error(f\"No\
    \ Python files found in {source}\")\n\n    # Check contents rather than mtimes:\
    \ pre-commit temporarily restores files.\n    digest = hashlib.sha256()\n    for\
    \ path in [Path(__file__).resolve(), exclude_file, *files]:\n        digest.update(path.relative_to(ROOT).as_posix().encode())\n\
    \        digest.update(b\"\\0\")\n        digest.update(path.read_bytes())\n \
    \       digest.update(b\"\\0\")\n    source_hash = digest.hexdigest()\n    cache_key\
    \ = hashlib.sha256(str(output).encode()).hexdigest()\n    cache_path = ROOT /\
    \ \"build/notebook\" / f\"{cache_key}.json\"\n    try:\n        cache = json.loads(cache_path.read_text(encoding=\"\
    utf-8\"))\n    except (OSError, ValueError):\n        cache = {}\n    if (\n \
    \       not args.force\n        and isinstance(cache, dict)\n        and cache.get(\"\
    source\") == source_hash\n        and output.is_file()\n        and cache.get(\"\
    pdf\") == hashlib.sha256(output.read_bytes()).hexdigest()\n    ):\n        if\
    \ args.stage:\n            subprocess.run([\"git\", \"-C\", str(ROOT), \"add\"\
    , \"--\", str(output)], check=True)\n        print(f\"Up to date: {output}\")\n\
    \        return\n\n    if not shutil.which(\"lualatex\"):\n        parser.error(\"\
    lualatex is required (see README.md)\")\n    from pygments import highlight\n\
    \    from pygments.formatters import LatexFormatter\n    from pygments.lexers\
    \ import PythonLexer\n\n    # Suppress volatile PDF metadata, including the trailer\
    \ ID derived from\n    # the randomly named temporary build directory.\n    preamble\
    \ = r\"\"\"\\pdfvariable suppressoptionalinfo 767\\relax\n\\documentclass[a4paper,9pt,twocolumn]{extarticle}\n\
    \\usepackage[margin=10mm,top=9mm,bottom=9mm,footskip=5mm]{geometry}\n\\usepackage{luatexja-fontspec}\n\
    \\setmainjfont{IPAexGothic}\n\\setsansjfont{IPAexGothic}\n\\setmonojfont{IPAexGothic}\n\
    \\usepackage{fvextra}\n\\usepackage{xcolor}\n\\usepackage{fancyhdr}\n\\usepackage[hidelinks,unicode]{hyperref}\n\
    \\pagestyle{fancy}\n\\fancyhf{}\n\\renewcommand{\\headrulewidth}{0pt}\n\\fancyfoot[R]{\\\
    fontsize{11}{13}\\selectfont\\thepage}\n\\setlength{\\columnsep}{7mm}\n\\setcounter{tocdepth}{2}\n\
    \\begin{document}\n\\pdfbookmark[0]{Python Algorithm Library}{title}\n\\makeatletter\n\
    \\@starttoc{toc}\n\\makeatother\n\"\"\"\n    with tempfile.TemporaryDirectory(prefix=\"\
    python-notebook-\") as directory:\n        work = Path(directory)\n        formatter\
    \ = LatexFormatter(\n            style=\"friendly\",\n            verboptions=r\"\
    fontsize=\\fontsize{9}{9}\\selectfont,numbers=left,numbersep=3pt,breaklines=true,breakanywhere=true,tabsize=4\"\
    ,\n        )\n        parts = [\n            preamble.replace(\n             \
    \   r\"\\begin{document}\",\n                formatter.get_style_defs() + \"\\\
    n\" + r\"\\begin{document}\",\n            )\n        ]\n        category = None\n\
    \        for path in files:\n            relative = path.relative_to(source)\n\
    \            group = relative.parent.as_posix()\n            if group in {\".\"\
    , \"gen\"}:\n                group = \"Templates, gen\"\n            if group\
    \ != category:\n                category = group\n                parts.append(\n\
    \                    r\"\\section{\"\n                    + escape(group)\n  \
    \                  + \"}\\n\"\n                )\n            title = path.name\n\
    \            if relative.as_posix() in PARTIAL_CLASSES:\n                title\
    \ += \"\uFF08\u5DEE\u5206\uFF09\"\n            parts.append(r\"\\subsection{\"\
    \ + escape(title) + \"}\\n\")\n            # Pygments escapes TeX characters;\
    \ source code is never executed.\n            parts.append(\n                highlight(notebook_code(path,\
    \ relative), PythonLexer(), formatter)\n            )\n        parts.append(r\"\
    \\end{document}\")\n        (work / \"notebook.tex\").write_text(\"\".join(parts),\
    \ encoding=\"utf-8\")\n        # Two passes resolve the table of contents and\
    \ PDF links.\n        for _ in range(2):\n            result = subprocess.run(\n\
    \                [\n                    \"lualatex\",\n                    \"\
    -interaction=nonstopmode\",\n                    \"-halt-on-error\",\n       \
    \             \"notebook.tex\",\n                ],\n                cwd=work,\n\
    \                stdout=subprocess.PIPE,\n                stderr=subprocess.STDOUT,\n\
    \                text=True,\n                env={**os.environ, \"SOURCE_DATE_EPOCH\"\
    : \"0\", \"FORCE_SOURCE_DATE\": \"1\"},\n            )\n            if result.returncode:\n\
    \                raise SystemExit(result.stdout)\n        output.parent.mkdir(parents=True,\
    \ exist_ok=True)\n        shutil.copyfile(work / \"notebook.pdf\", output)\n \
    \   cache_path.parent.mkdir(parents=True, exist_ok=True)\n    cache_path.write_text(\n\
    \        json.dumps({\"source\": source_hash, \"pdf\": hashlib.sha256(output.read_bytes()).hexdigest()}),\n\
    \        encoding=\"utf-8\",\n    )\n    if args.stage:\n        subprocess.run([\"\
    git\", \"-C\", str(ROOT), \"add\", \"--\", str(output)], check=True)\n    print(f\"\
    Created {output} ({len(files)} files)\")\n\n\nif __name__ == \"__main__\":\n \
    \   main()\n"
  dependsOn: []
  isVerificationFile: false
  path: tools/build_notebook.py
  requiredBy: []
  timestamp: '2026-11-22 20:55:47+09:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: tools/build_notebook.py
layout: document
redirect_from:
- /library/tools/build_notebook.py
- /library/tools/build_notebook.py.html
title: tools/build_notebook.py
---
