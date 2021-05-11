#!/usr/bin/env bash

#first set the working directory 
# cd 'your path'

VENVNAME=collocation_environment

python3 -m venv $VENVNAME
source $VENVNAME/bin/activate
pip install --upgrade pip

pip install ipython
pip install jupyter
python -m ipykernel install --user --name=$VENVNAME

# check and install requirements
test -f requirements.txt && pip install -r requirements.txt

#then deactivate the environment
deactivate
echo "build $VENVNAME"

#!/usr/bin/env bash


