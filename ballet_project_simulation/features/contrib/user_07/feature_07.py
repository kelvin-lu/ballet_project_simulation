from ballet import Feature
import sklearn.impute


input = ["Mas Vnr Area"]
transformer = sklearn.impute.SimpleImputer(strategy="mean")
name = "Imputed masonry veneer area in square feet"
feature = Feature(input=input, transformer=transformer, name=name)
