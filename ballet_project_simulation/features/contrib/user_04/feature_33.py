from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["Exterior 1st"]
transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Exterior covering on house type"
feature = Feature(input=input, transformer=transformer, name=name)
