#!/usr/bin/env python

""" Execute one Jupyter notebook and write the executed copy, with outputs,
to the target path. Invoked by the generator as
nb_execute.py <input.ipynb> <output.ipynb>.

The demos read their data files (csv, npy, png, wav) by bare relative name
and some of them also write files next to themselves. nbconvert starts the
kernel in the directory of the notebook it executes, whatever the process
cwd is, so running the source notebook directly would write into the source
tree. Instead the notebook and the data files next to it are copied to a
temporary directory and the copy is executed there; only the executed
notebook is copied to the output path. Neither the source tree nor out/
gets anything else. """

import os
import shutil
import subprocess
import sys
import tempfile


def main():
    """ main entry point """
    source, output = sys.argv[1], sys.argv[2]
    source_dir = os.path.dirname(os.path.abspath(source))
    os.makedirs(os.path.dirname(os.path.abspath(output)), exist_ok=True)
    with tempfile.TemporaryDirectory() as scratch:
        for name in os.listdir(source_dir):
            path = os.path.join(source_dir, name)
            if os.path.isfile(path) and not name.endswith(".ipynb"):
                shutil.copy2(path, os.path.join(scratch, name))
        notebook = os.path.join(scratch, os.path.basename(source))
        shutil.copy2(source, notebook)
        ret = subprocess.call([
            "jupyter",
            "nbconvert",
            "--to",
            "notebook",
            "--execute",
            "--inplace",
            notebook,
        ], cwd=scratch)
        if ret != 0:
            sys.exit(ret)
        shutil.copy2(notebook, output)


if __name__ == "__main__":
    main()
