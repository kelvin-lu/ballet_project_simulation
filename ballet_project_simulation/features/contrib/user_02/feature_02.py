from ballet import Feature
import sklearn.preprocessing


input = ["Mo Sold"]
transformer = sklearn.preprocessing.OneHotEncoder()
name = "Month Sold Categorical"
feature = Feature(input=input, transformer=transformer, name=name)
