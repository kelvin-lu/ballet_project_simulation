from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Lot Shape"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="missing"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "General shape of property type"
feature = Feature(input=input, transformer=transformer, name=name)
