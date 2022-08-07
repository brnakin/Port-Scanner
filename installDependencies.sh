#!/bin/sh

Green='\033[1;32m'

sudo apt install python3-pip
pip3 install sockets
pip3 install IPy
pip3 install colored
pip3 install termcolor

echo "${Green}[+]The dependencies have been successfully installed!"
