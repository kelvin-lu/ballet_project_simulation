from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["Bsmt Exposure"]
transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Basement walkout or garden level walls type"
feature = Feature(input=input, transformer=transformer, name=name)
