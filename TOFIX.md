# TOFIX

Findings from a code scan on 2026-10-04.

## Medium

- `rsconstruct.toml:27` - the ruff processor scans only `.py` (rsconstruct's default `src_extensions`), so none of the ~30 `.ipynb` demos under `src/` get linted, even though ruff supports notebooks. Running ruff directly already finds an unfixed I001 in `src/scipy/demos/scipy_examples.ipynb` cell 19. Set `src_extensions = [".py", ".ipynb"]` for ruff and fix the import order.
- `pyproject.toml:28` - `mypy_path = "src:python:scripts"` names a `python/` directory that does not exist. Drop `python` from the path.
- `rsconstruct.toml:49` - only notebooks are executed (the `notebooks` generator). The ~35 standalone `.py` demos (`src/matplotlib/demos/pylab_demo*.py`, `src/scipy/demos/*.py`, `src/numpy/demos/*.py`) are only linted, never run, so API breakage in matplotlib/scipy goes unnoticed. This is also the open item in `doc/TODO.txt:1`. Add a generator or checker that runs each script headless (`MPLBACKEND=Agg`) from an out/ copy, the way `scripts/nb_execute.py` does.

## Low

- `rsconstruct.toml:30` - `batch = false` on the ruff processor has no comment, and the comment right below it (lines 32-35, about batch staying at the default) belongs to mypy, so it reads as if it explains the ruff line. Add a reason for the ruff override or remove it, and keep the mypy comment next to `[processor.mypy]`.
- `doc/TODO.txt:3` - "stop collecting .py files from the .ipynb_checkpoints folders" is stale: no checkpoint files are tracked, and the ruff/mypy processors scan only `src`, `scripts` and `config`. Remove the item.
- `src/numpy/demos/my.html` - a 7-line "life is good" page that no demo, notebook or doc references. Delete it, or tie it to the demo that writes HTML.
- `pyproject.toml:19` - `pytest` is in the dev group, but the repo has no tests and no pytest processor. Drop it, or use it for the `.py` demo runner above.
