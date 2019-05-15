from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["Garage Finish"]
transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Garage finish type"
feature = Feature(input=input, transformer=transformer, name=name)
