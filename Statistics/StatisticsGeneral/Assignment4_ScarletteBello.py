#Scarlette Bello       c0860234
#Association rules


import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.frequent_patterns import association_rules



data = pd.read_csv('assignment4data.csv')
print(data,'\n')


# Data Coversion
basket_sets = pd.get_dummies(data)
print(basket_sets,'\n')


# Support Calculation
data_apriori = apriori(basket_sets, min_support=0.02, use_colnames=True)
df = basket_sets
print(data_apriori, '\n')

frequent_itemsets = apriori(df, min_support=0.002, use_colnames=True)
frequent_itemsets['length'] = frequent_itemsets['itemsets'].apply(lambda x: len(x))
print(frequent_itemsets)

frequent_itemsetsmorethree = frequent_itemsets[frequent_itemsets['length'] >= 3]
print(frequent_itemsetsmorethree)


# # Association Rules
rules_conf = association_rules(frequent_itemsets, metric="confidence", min_threshold=0.5)
print(rules_conf)


## Lift
rules_lift = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
print(rules_lift.head())


# ## Lift and Confidence
lift_conf =  rules_conf[(rules_conf['lift'] >= 5) & (rules_conf['confidence']>= 0.5)]
print(lift_conf)


print(rules_conf[['consequents','confidence','antecedent support']])