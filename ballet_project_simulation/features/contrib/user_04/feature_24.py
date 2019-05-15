from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["Pool QC"]
transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Pool quality type"
feature = Feature(input=input, transformer=transformer, name=name)
