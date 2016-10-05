#!/bin/sh

APP_HOME=`pwd`/spaceformatter
BIN_PATH=${APP_HOME}/bin
LIB_PATH=${APP_HOME}/lib
INIT_FILE="__init__.py"

echo "Starting installation of spaceformatter"
echo ""
echo "pwd is \'`pwd`\'"

echo "mkdir -p ${BIN_PATH}"
mkdir -p ${BIN_PATH}
echo "mkdir -p ${BIN_PATH}"
mkdir -p ${LIB_PATH}

echo "touch ${LIB_PATH}/${INIT_FILE}"
touch ${LIB_PATH}/${INIT_FILE}
echo "mv space_formatter.py ${LIB_PATH}"
mv space_formatter.py ${LIB_PATH}

echo "touch ${BIN_PATH}/${INIT_FILE}"
touch ${BIN_PATH}/${INIT_FILE}
echo "mv file_input_formatter.py ${BIN_PATH}"
mv file_input_formatter.py ${BIN_PATH}
echo "mv tkinter_formatter.py ${BIN_PATH}"
mv tkinter_formatter.py ${BIN_PATH}

echo "Installation Success"
