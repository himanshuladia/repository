#!/bin/bash

echo "Creating new anaconda environment himanshuladia"
conda create -n himanshuladia python=3.6
source activate himanshuladia
pip install -r requirements.txt