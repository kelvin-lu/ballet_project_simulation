from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Sale Type"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Sale Type type"
feature = Feature(input=input, transformer=transformer, name=name)
