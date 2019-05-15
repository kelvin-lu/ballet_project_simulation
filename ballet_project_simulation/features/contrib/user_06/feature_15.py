from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["Utilities"]
transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Utilities type"
feature = Feature(input=input, transformer=transformer, name=name)
