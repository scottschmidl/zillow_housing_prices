# Zillow Housing Price Project
This repo contains my Zillow housing prices regression project with Codeup.

## About

### Goal
The goal of this project is to understand what affects the price of a house on Zillow and predict, within a range, the price of a house.

### Description
I want to predict housing prices as accuractely as possible to help sellers and buyers maximize their quality of life.

### Initial Questions
1) Does a correlation exist between square feet and price?
2) Is there a correlation between number of bathrooms and price?
3) Is there a correlation between number of bedroooms and price?
4) Do houses in Los Angeles cost more than Orange County or Ventura?

### Data Dictionary
<table>
<thead><tr>
<th>Target</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>home_tax_value</td>
<td>Home price</td>
</tr>
</tbody>
</table>

<table>
<thead><tr>
<th>Variable</th>
<th>Meaning</th>
</tr>
</thead>
<tbody>
<tr>
<td>bedrooms</td>
<td>How many bedrooms are in a house</td>
</tr>
<tr>
<td>bathrooms</td>
<td>How many bathrooms are in a house</td>
</tr>
<tr>
<td>square_feet</td>
<td>Size of the house</td>
</tr>
<tr>
<td>year_built</td>
<td>Year in which the house was built</td>
</tr>
<tr>
<td>fips</td>
<td>County Code</td>
</tr>
<tr>
<td>county</td>
<td>County in which the house is located</td>
</tr>
</tbody>
</table>

### Steps to Reproduce
You will need an env.py file that contains the hostname, username, and password of the MySQL database that contains the Zillow Housing data. The env.py file will need to be in the repository and filename verified or placed in the git ignore. Clone this repo and ensure wrangle.py and prepare.py are on your local machine. Additionally, verify env.py is in the git ignore to ensure security of your login information. The technologies used in this project are Python 3.8.11, Pandas 1.3.4, MatPlotLib 3.4.3, Seaborn 0.11.2, Scipy 1.7.1, and SkLearn 1.0.1. The notebook named report.ipynb should run.

### Plan
The plan is to wrangle the data either from a CSV or the MySQL database and perform some preparation steps. Then, I  will do some visualizations and compliment them with some statistical tests. Finally, I will do some regression machine learning using Lasso Lars, Linear Regression, and Tweedie Regressor. I will fit on the training data and check for overfitting on with the validation data. I will then pick the best model to test and move into production. I will then discuss some recommendations and next steps I would like to do with this project.

