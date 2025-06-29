""" python deps for this project """

install_requires: list[str] = [
    "scikit-learn",
    "scikit-image",
    "pandas",
    "numpy",
    "matplotlib",
    "jupyter",
]
build_requires: list[str] = [
    "pycmdtools",
    "pymakehelper",
    "pydmt",
    "mypy",
    "pylint",
]
requires = install_requires + build_requires
