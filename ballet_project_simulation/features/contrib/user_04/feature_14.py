from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Street"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="missing"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Type of road access to property"
feature = Feature(input=input, transformer=transformer, name=name)
