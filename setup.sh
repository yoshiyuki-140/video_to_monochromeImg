#!/bin/bash

sudo apt update && sudo apt upgrade -y
sudo apt install python3
pip install -r reqirements.txt
python3 ./main.py