from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["Garage Qual"]
transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Garage quality type"
feature = Feature(input=input, transformer=transformer, name=name)
