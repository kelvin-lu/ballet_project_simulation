from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Lot Config"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Lot Config type"
feature = Feature(input=input, transformer=transformer, name=name)
