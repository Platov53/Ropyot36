#!/bin/bash

SCRIPT_DIR=$(dirname "$(readlink -f "$0")")
cd "$SCRIPT_DIR"

source ./venv/bin/activate

pip install -r requeriments.txt

python3 src/Ropyot36.py

deactivate