from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["BsmtFin Type 2"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "BsmtFin Type 2 type"
feature = Feature(input=input, transformer=transformer, name=name)
