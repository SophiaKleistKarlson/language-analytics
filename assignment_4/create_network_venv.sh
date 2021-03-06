#!/usr/bin/env bash

#first set the working directory 
# cd 'your path'

VENVNAME=network_venv

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

pip install ipython
pip install jupyter

python -m ipykernel install --user --name=$VENVNAME

test -f requirements.txt && pip install -r requirements.txt
python -m spacy download en_core_web_sm

deactivate
echo "build $VENVNAME"

