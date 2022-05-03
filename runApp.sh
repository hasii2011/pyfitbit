#!/usr/local/bin/bash
# Assumes we are at the project
# Asmes the appropriate virtual environment is set up
#
DB_PATH=$(pwd)
LOG_CONFIG_PATH=$(pwd)

export DB_PATH
export LOG_CONFIG_PATH

python -m org.hasii.pythonflask.fitbitapp
