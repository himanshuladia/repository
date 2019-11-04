# Author : Himanshu Ladia
# Date : 30/10/2019

# Folder/File Descriptions -
1. logs - Contains jupyter notebooks of all the data preparation and model prototyping in python
2. model - Contains pickle of model, data mean, data std, and labels
3. notebook.ipynb - Jupyter notebook of the final data preparation and model in python
4. predict.py - Contains predict(folderpath) function which takes the path to test folder and generates output.csv
5. README.txt - This file
6. requirements.txt - Used by script.sh. Contains names of python packages required to run the predict.py function. 
7. script.sh - Bash script to create conda environment and install required packages.

# How to run -
1. script.sh - Grant executing permissions using "chmod +x script.sh". Run using "./script.sh" on terminal. A conda env "himanshuladia" will be created. Run "conda activate himanshuladia" on terminal to activate the environment.
2. predict.py - Run the predict() function in main and pass folderpath as arguement. This will generate output.csv.
3. notebook.py - Run as a jupyter notebook.