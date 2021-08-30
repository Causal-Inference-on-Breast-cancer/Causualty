# Breast Cancer
## Introduction
<p> 
A common frustration in the industry, especially when it comes to getting business insights from tabular data, is that the most interesting questions (from their perspective) are often not answerable with observational data alone. These questions can be similar to:
“What will happen if I halve the price of my product?”
“Which clients will pay their debts only if I call them?”
Judea Pearl and his research group have developed in the last decades a solid theoretical framework to deal with that, but the first steps toward merging it with mainstream machine learning are just beginning. 

The causal graph is a central object in the framework mentioned above, but it is often unknown, subject to personal knowledge and bias, or loosely connected to the available data.
</p>
<p>
Bayesian Network (BN), is a probabilistic weighted DAG where nodes represent variables, edges represent the causal relationships between variables. We aim to use a Bayesian Network to build a model that diagnoses breast cancer given the relevant features extracted from medical images.
</p>

## Code
The code of our analysis can be found in the **notebooks** folder. The data loading, visualization, and modelling can be found in the **Data Exploration, ML and Causal Modeling.ipynb** jupyter notebook. The notebook also contains the code for training six types of classification models.
<ol>
<li>Logistic Regression Classification :- Best Accuracy: 96.5% </li>
<li>Random Forest Classification :- Best Accuracy: 94.7%</li>
<li>SVM Classification :- Best Accuracy: 96.49%</li>
<li>3 Layer DNN :- Best Accuracy: 96.49%</li>
<li>Large Bayesian Network:- Best Accuracy: 87.7%</li>
<li>Simplified Bayesian Network:- Best Accuracy: 89.5%</li>
</ol>

The **scripts** folder contains the data loading and preprocessing functions. 

## Dependencies
To install the necessary dependencies, execute the command 
```$ pip install -r requirements.txt"```
