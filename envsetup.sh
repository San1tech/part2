#!/bin/sh

if [ -d "env" ] 
then
    echo "Python virtual environment exists." 
else
    sudo apt install python3.8 venv env
fi

source Scripts/activate


pip3 install -r requirements.txt

if [ -d "logs" ] 
then
    echo "Log folder exists." 
else
    mkdir logs
    touch logs/error.log logs/access.log
fi

sudo chmod -R 777 logs
