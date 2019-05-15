from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["Kitchen Qual"]
transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Kitchen quality type"
feature = Feature(input=input, transformer=transformer, name=name)
