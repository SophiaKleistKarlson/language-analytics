#!/usr/bin/env bash

#first write this:
#cd cds-language/src

VENVNAME=headline_sentiment_environment

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

pip install ipython
pip install jupyter
python -m ipykernel install --user --name=$VENVNAME

test -f requirements.txt && pip install -r requirements.txt
python -m spacy download en_core_web_sm

# then this: (in here, it would be src instead of folder below
python3 folder/keyword_headline_sentiment.py

#then deactivate
deactivate
echo "build $VENVNAME"
