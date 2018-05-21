#!/usr/local/bin/bash
#
#Text color variables
#
fgBlack=$(tput setaf 0) 	# black
fgRed=$(tput setaf 1) 		# red
fgGreen=$(tput setaf 2) 	# green
fgYellow=$(tput setaf 3) 	# yellow
fgBlue=$(tput setaf 4) 		# blue
fgMagenta=$(tput setaf 5) 	# magenta
fgCyan=$(tput setaf 6) 		# cyan
fgWhite=$(tput setaf 7) 	# white
#
txBold=$(tput bold)   		# bold
txHalf=$(tput dim)    		# half-bright
txUnderline=$(tput smul)   	# underline
txEndUnder=$(tput rmul)   	# exit underline
txReverse=$(tput rev)    	# reverse
txStandout=$(tput smso)   	# standout
txEndStand=$(tput rmso)   	# exit standout
txReset=$(tput sgr0)   	# reset attributes
#
# Assumes this script executes from root of project
#
source ./venv-pyflask/bin/activate

cd org/hasii/pythonflask/
export FULL_PATH=`pwd`
export FLASK_APP=$FULL_PATH/fitbitapp.py
cd -
export DB_PATH=`pwd`
export LOG_CONFIG_PATH=`pwd`

tput clear

echo "Full Path:       ${fgWhite}$FULL_PATH${txReset}"
echo "Flask App:       ${fgWhite}$FLASK_APP${txReset}"
echo "DB Path:         ${fgWhite}$DB_PATH${txReset}"
echo "Log Config Path: ${fgWhite}$LOG_CONFIG_PATH${txReset}"

echo "Log Config Path: ${fgWhite}$LOG_CONFIG_PATH${txReset}"
flask db init

echo "Log Config Path: ${fgWhite}$LOG_CONFIG_PATH${txReset}"
flask db migrate -m "FitBitRecord"

echo "Log Config Path: ${fgWhite}$LOG_CONFIG_PATH${txReset}"
flask db upgrade


