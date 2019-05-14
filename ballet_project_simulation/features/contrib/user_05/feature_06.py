from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["Mas Vnr Type"]
transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Masonry veneer type"
feature = Feature(input=input, transformer=transformer, name=name)
