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
txReset=$(tput sgr0)   	    # reset attributes

function isValid() {

    if [ $1 -gt 0 ]; then
        printf "${fgRed}ERROR: ${2}${txReset}\n"
        exit $2
    else
    	shift
    	shift
    	printf "${fgMagenta}$*: ${fgWhite}Ok\n"
    fi
}
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

printf "Full Path:       ${fgWhite}%s${txReset}\n" $FULL_PATH
printf "Flask App:       ${fgWhite}%s${txReset}\n" $FLASK_APP
printf "DB Path:         ${fgWhite}%s${txReset}\n" $DB_PATH
printf "Log Config Path: ${fgWhite}%s${txReset}\n" $LOG_CONFIG_PATH


flask db init &>/dev/null
stat=$?
isValid $stat 66 "Initialize Database"

flask db migrate -m "FitBitRecord" &>/dev/null
stat=$?
isValid $stat 77 "Create Migration Scripts"

flask db upgrade &>/dev/null
stat=$?
isValid $stat 88 "Create Database"

