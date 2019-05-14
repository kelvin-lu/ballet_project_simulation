from ballet import Feature
import sklearn.impute


input = ["Lot Frontage"]
transformer = sklearn.impute.SimpleImputer(strategy="mean")
name = "Lot Frontage Fill"
feature = Feature(input=input, transformer=transformer, name=name)
