#!/bin/sh
tree -l 8 node_modules --fullpath --noreport -o tree.txt
python parse-path.py
less tree.txt
