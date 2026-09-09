#!/usr/bin/env python

""" Execute one Jupyter notebook and write the executed copy, with outputs,
to the target path. Invoked by the generator as
nb_execute.py <input.ipynb> <output.ipynb>.

The demos read their data files (csv, npy, png, wav) by bare relative name
and some of them also write files next to themselves. nbconvert starts the
kernel in the directory of the notebook it executes, whatever the process
cwd is, so running the source notebook directly would write into the source
tree. Instead the notebook and the data files next to it are copied to the
output directory and the copy is executed in place: the source tree is
never written to, and everything the run produces lands under out/. """

import os
import shutil
import subprocess
import sys


def main():
    """ main entry point """
    source, output = sys.argv[1], sys.argv[2]
    source_abs = os.path.abspath(source)
    output_abs = os.path.abspath(output)
    source_dir = os.path.dirname(source_abs)
    output_dir = os.path.dirname(output_abs)
    os.makedirs(output_dir, exist_ok=True)
    for name in os.listdir(source_dir):
        path = os.path.join(source_dir, name)
        if os.path.isfile(path) and not name.endswith(".ipynb"):
            shutil.copy2(path, os.path.join(output_dir, name))
    shutil.copy2(source_abs, output_abs)
    sys.exit(subprocess.call([
        "jupyter",
        "nbconvert",
        "--to",
        "notebook",
        "--execute",
        "--inplace",
        output_abs,
    ], cwd=output_dir))


if __name__ == "__main__":
    main()
