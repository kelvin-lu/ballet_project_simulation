from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Mas Vnr Type"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Mas Vnr Type type"
feature = Feature(input=input, transformer=transformer, name=name)
