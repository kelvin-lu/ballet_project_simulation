from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["Exterior 2nd"]
transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Exterior covering on house (if more than one material) type"
feature = Feature(input=input, transformer=transformer, name=name)
