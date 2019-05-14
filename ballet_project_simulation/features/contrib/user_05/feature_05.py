from ballet import Feature
from sklearn.preprocessing import OneHotEncoder


input = ["Overall Cond"]
transformer = OneHotEncoder()
name = "Overall condition"
feature = Feature(input=input, transformer=transformer, name=name)
