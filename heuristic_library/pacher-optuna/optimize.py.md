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
    \ Any\n\nimport optuna\n\n\n# TODO: Write parameter suggestions here\ndef generate_params(trial:\
    \ optuna.trial.Trial) -> dict[str, str]:\n    # for more information, see https://optuna.readthedocs.io/en/stable/reference/generated/optuna.trial.Trial.html\n\
    \    params = {\n        \"start_temp\": str(trial.suggest_float(\"start_temp\"\
    , 150, 300)),\n        \"end_temp\": str(trial.suggest_float(\"end_temp\", 0.1,\
    \ 20)),\n    }\n\n    return params\n\n\n# TODO: Customize the score extraction\
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
    \ n_trials=100)\n\n\nclass Objective:\n    def __init__(self) -> None:\n     \
    \   pass\n\n    def __call__(self, trial: optuna.trial.Trial) -> float:\n    \
    \    params = generate_params(trial)\n        env = os.environ.copy()\n      \
    \  env.update(params)\n\n        scores = []\n\n        cmd = [\n            \"\
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
    optuna-study\",\n    pruner=optuna.pruners.WilcoxonPruner(),\n    sampler=optuna.samplers.TPESampler(),\n\
    )\n\nrun_optimization(study)\n\nprint(f\"best params = {study.best_params}\")\n\
    print(f\"best score  = {study.best_value}\")\n"
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
