from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Fence"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="missing"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Fence quality type"
feature = Feature(input=input, transformer=transformer, name=name)
