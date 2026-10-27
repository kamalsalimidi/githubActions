#!/bin/sh
set -eu
python3 -m compileall -q app.py
python3 -m unittest -v
mkdir -p dist
tar -czf dist/app.tgz app.py
mkdir test2
mkdir test
