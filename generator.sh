#!/usr/bin/env bash

shellcheck disable=SC2164
cd C:\Users\lwsmu\OneDrive\Documents\Third Year-Second Sem\Computer Graphics\massive-dataset-lab

# Activate the virtual environment
C:\Users\lwsmu\OneDrive\Documents\Third_Year-Second_Sem\Computer_Graphics\massive-dataset-lab\venv\Scripts\Activate

python -c 'import functions; functions.filtered_languages()'
python -c 'import functions; functions.english_translations_to_json()'

# Deactivate the virtual environment
deactivate