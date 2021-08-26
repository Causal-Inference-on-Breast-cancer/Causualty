# Casualty
Perform Casualty Inference on Brest cancer data set using Judea Pearl and his research groups framework.

# Table of content
- [Introduction](#introduction)
- [Instalation](#instalation)
- [Folders](#folders)
  - [data](#data)
  - [challenge-document](#challenge-document)
  - [myscripts](#myscripts)
  - [notebooks](#notebooks)
  - [tests](#tests)

## Introduction
A common frustration in the industry, especially when it comes to getting business insights from tabular data, is that the most interesting questions (from their perspective) are often not answerable with observational data alone. These questions can be similar to:
- “What will happen if I halve the price of my product?”
- “Which clients will pay their debts only if I call them?”

Judea Pearl and his research group have developed in the last decades a solid theoretical framework to deal with that, but the first steps toward merging it with mainstream machine learning are just beginning.

## Installation
- Install Packages
```
git clone 
cd Causality
pip install -r requriements.txt
```

- Jupyter Noteboks
```
cd notebooks
jupyter notebook
```

## Folders
Folder structure of the project try to follwo more organized and modularized format.

#### data: 
folder containing the data set of breast cancer downloaded from [kaggle](https://www.kaggle.com/uciml/breast-cancer-wisconsin-data). The data set contain about 570 rows and 33 columns.


#### challenge-document: 
this folder contain pdf file with the project description and tasks to perform on the data set. the document is provided form 10 academy training team.

#### myscripts:
This folder contain python modules. The main purpose of this forlder is for code modularization and increase code reusability. 

- ```def_clean.py``` : python module concerned with cleaning data frame. operation include filling null values, droping columns fixing outliers and others.
- ```df_info.py```: python module concerned in providing information about the data frame. operations include null percentage, information, columns list and others.
- ```file.py```: python module concerned with reading csv files from file and haldeling errors while reading the file.
- ```plotting.py``` : python module concerned with generating graphs and plots from provided data frame.

#### notebooks:
This folder contain notebooks files that are necessary for data exploration and to get more indepth analysis on the data set.
- ```0_EDA``` : Notebook file for making exploratory data analysis and help us understand more about the data.

#### tests:
This folder contain test files for critical part of the application.

## Technologies uses
- ```DVC``` : for remote storage and data versioning.
- ```CML```: for getting model performance result when we push our code. 