from ballet import Feature
import sklearn.impute
import sklearn.preprocessing


input = ["BsmtFin Type 1"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Rating of basement finished area type"
feature = Feature(input=input, transformer=transformer, name=name)
