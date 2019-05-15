from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["Fireplace Qu"]
transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Fireplace quality type"
feature = Feature(input=input, transformer=transformer, name=name)
