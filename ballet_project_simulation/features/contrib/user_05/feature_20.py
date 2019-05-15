from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["Sale Type"]
transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Sale type"
feature = Feature(input=input, transformer=transformer, name=name)
