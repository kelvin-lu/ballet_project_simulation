from ballet import Feature
import ballet.eng
import sklearn.impute
import sklearn.preprocessing

input = ["Bsmt Cond"]

transformer = [
    sklearn.impute.SimpleImputer(strategy="most_frequent"),
    sklearn.preprocessing.OneHotEncoder(),
]

name = "Imputed basement condition type"

feature = Feature(input=input, transformer=transformer, name=name)
