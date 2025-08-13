---
data:
  _extendedDependsOn: []
  _extendedRequiredBy: []
  _extendedVerifiedWith: []
  _isVerificationFailed: false
  _pathExtension: py
  _verificationStatusIcon: ':warning:'
  attributes:
    links:
    - https://optuna.readthedocs.io/en/stable/reference/generated/optuna.trial.Trial.html
    - https://tech.preferred.jp/ja/blog/wilcoxonpruner/
  bundledCode: "Traceback (most recent call last):\n  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/documentation/build.py\"\
    , line 71, in _render_source_code_stat\n    bundled_code = language.bundle(stat.path,\
    \ basedir=basedir, options={'include_paths': [basedir]}).decode()\n          \
    \         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n\
    \  File \"/opt/hostedtoolcache/Python/3.11.0/x64/lib/python3.11/site-packages/onlinejudge_verify/languages/python.py\"\
    , line 96, in bundle\n    raise NotImplementedError\nNotImplementedError\n"
  code: "import json\nimport math\nimport os\nimport subprocess\nfrom typing import\
    \ Any\n\nimport optuna\nimport optunahub\nimport optuna.visualization\n\n# TODO:\
    \ Write parameter suggestions here\ndef generate_params(trial: optuna.trial.Trial)\
    \ -> dict[str, str]:\n    # for more information, see https://optuna.readthedocs.io/en/stable/reference/generated/optuna.trial.Trial.html\n\
    \    params = {\n        \"start_temp\": str(trial.suggest_float(\"start_temp\"\
    , 50, 250)),\n        \"end_temp\": str(trial.suggest_float(\"end_temp\", 0.01,\
    \ 15)),\n    }\n\n    return params\n\n\n# TODO: Customize the score extraction\
    \ code here\ndef extract_score(result: dict[str, Any]) -> float:\n    absolute_score\
    \ = result[\"score\"]  # noqa: F841\n    log10_score = math.log10(absolute_score)\
    \ if absolute_score > 0.0 else 0.0  # noqa: F841\n    relative_score = result[\"\
    relative_score\"]  # noqa: F841\n\n    score = absolute_score  # for absolute\
    \ score problems\n    # score = log10_score       # for relative score problems\
    \ (alternative)\n    # score = relative_score    # for relative score problems\n\
    \n    return score\n\n\n# TODO: Set the direction to minimize or maximize\ndef\
    \ get_direction() -> str:\n    # direction = \"minimize\"\n    direction = \"\
    maximize\"\n    return direction\n\n\n# TODO: Set the timeout (seconds) or the\
    \ number of trials\ndef run_optimization(study: optuna.study.Study) -> None:\n\
    \    # study.optimize(Objective(), timeout=600)\n    study.optimize(Objective(),\
    \ n_trials=50)\n\n\nclass Objective:\n    def __init__(self) -> None:\n      \
    \  pass\n\n    def __call__(self, trial: optuna.trial.Trial) -> float:\n     \
    \   params = generate_params(trial)\n        env = os.environ.copy()\n       \
    \ env.update(params)\n\n        scores = []\n\n        cmd = [\n            \"\
    pahcer\",\n            \"run\",\n            \"--json\",\n            \"--shuffle\"\
    ,\n            \"--no-result-file\",\n            \"--freeze-best-scores\",\n\
    \        ]\n\n        if trial.number != 0:\n            cmd.append(\"--no-compile\"\
    )\n\n        process = subprocess.Popen(\n            cmd,\n            stdout=subprocess.PIPE,\n\
    \            env=env,\n        )\n\n        # see also: https://tech.preferred.jp/ja/blog/wilcoxonpruner/\n\
    \        for line in process.stdout:\n            result = json.loads(line)\n\n\
    \            # If an error occurs, stop the process and raise an exception\n \
    \           if result[\"error_message\"] != \"\":\n                process.send_signal(subprocess.signal.SIGINT)\n\
    \                raise RuntimeError(result[\"error_message\"])\n\n           \
    \ score = extract_score(result)\n            seed = result[\"seed\"]\n       \
    \     scores.append(score)\n            trial.report(score, seed)\n\n        \
    \    if trial.should_prune():\n                print(f\"Trial {trial.number} pruned.\"\
    )\n                process.send_signal(subprocess.signal.SIGINT)\n\n         \
    \       objective_value = sum(scores) / len(scores)\n                is_better_than_best\
    \ = (\n                    trial.study.direction == optuna.study.StudyDirection.MINIMIZE\n\
    \                    and objective_value < trial.study.best_value\n          \
    \      ) or (\n                    trial.study.direction == optuna.study.StudyDirection.MAXIMIZE\n\
    \                    and objective_value > trial.study.best_value\n          \
    \      )\n\n                if is_better_than_best:\n                    # Avoid\
    \ updating the best value\n                    raise optuna.TrialPruned()\n  \
    \              else:\n                    # It is recommended to return the value\
    \ of the objective function at the current step\n                    # instead\
    \ of raising TrialPruned.\n                    # This is a workaround to report\
    \ the evaluation information of the pruned Trial to Optuna.\n                \
    \    return sum(scores) / len(scores)\n\n        return sum(scores) / len(scores)\n\
    \n\nstudy = optuna.create_study(\n    direction=get_direction(),\n    study_name=\"\
    optuna-study\",\n    pruner=optuna.pruners.WilcoxonPruner(),\n    sampler=optunahub.load_module(\n\
    \        \"samplers/auto_sampler\"\n    ).AutoSampler()  # \u5185\u90E8\u3067\u30A2\
    \u30EB\u30B4\u30EA\u30BA\u30E0\u3092\u81EA\u52D5\u9078\u629E\n)\n\n# pacher \u306E\
    \u30C9\u30AD\u30E5\u30E1\u30F3\u30C8\u901A\u308A\n# \u3053\u3063\u3061\u306E\u65B9\
    \u304C\u901F\u3044?\n# study = optuna.create_study(\n#     direction=get_direction(),\n\
    #     study_name=\"optuna-study\",\n#     pruner=optuna.pruners.WilcoxonPruner(),\n\
    #     sampler=optuna.samplers.TPESampler(),\n# )\n\nrun_optimization(study)\n\n\
    print(f\"best params = {study.best_params}\")\nprint(f\"best score  = {study.best_value}\"\
    )\n\nprint(\"Generating visualization files...\")\n\n# \u4FDD\u5B58\u7528\u30C7\
    \u30A3\u30EC\u30AF\u30C8\u30EA\u306E\u5B9A\u7FA9\noutput_dir = \"visualization\"\
    \n# \u30C7\u30A3\u30EC\u30AF\u30C8\u30EA\u304C\u5B58\u5728\u3057\u306A\u3044\u5834\
    \u5408\u306B\u81EA\u52D5\u3067\u4F5C\u6210\nos.makedirs(output_dir, exist_ok=True)\n\
    \n# 1. \u6700\u9069\u5316\u5C65\u6B74\u306E\u30D7\u30ED\u30C3\u30C8\nfig_history\
    \ = optuna.visualization.plot_optimization_history(study)\nfig_history.write_image(os.path.join(output_dir,\
    \ \"optimization_history.png\"))\n\n# 2. \u30D1\u30E9\u30E1\u30FC\u30BF\u91CD\u8981\
    \u5EA6\u306E\u30D7\u30ED\u30C3\u30C8\nfig_importance = optuna.visualization.plot_param_importances(study)\n\
    fig_importance.write_image(os.path.join(output_dir, \"param_importances.png\"\
    ))\n\n# 3. \u30B9\u30E9\u30A4\u30B9\u30D7\u30ED\u30C3\u30C8\nfig_slice = optuna.visualization.plot_slice(study)\n\
    fig_slice.write_image(os.path.join(output_dir, \"slice.png\"))\n\n# 4. \u4E2D\u9593\
    \u5024\u30D7\u30ED\u30C3\u30C8 (Pruning\u306E\u69D8\u5B50\u3092\u78BA\u8A8D)\n\
    fig_intermediate = optuna.visualization.plot_intermediate_values(study)\nfig_intermediate.write_image(os.path.join(output_dir,\
    \ \"intermediate_values.png\"))\n\nprint(f\"Visualization files saved as PNG in\
    \ '{output_dir}' directory.\")"
  dependsOn: []
  isVerificationFile: false
  path: heuristic_library/pacher-optuna/optimize.py
  requiredBy: []
  timestamp: '1970-01-01 00:00:00+00:00'
  verificationStatus: LIBRARY_NO_TESTS
  verifiedWith: []
documentation_of: heuristic_library/pacher-optuna/optimize.py
layout: document
redirect_from:
- /library/heuristic_library/pacher-optuna/optimize.py
- /library/heuristic_library/pacher-optuna/optimize.py.html
title: heuristic_library/pacher-optuna/optimize.py
---
