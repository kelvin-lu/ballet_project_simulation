from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Lot Shape"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Lot Shape type"
feature = Feature(input=input, transformer=transformer, name=name)
