from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Exterior 2nd"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Exterior covering on house (if more than one material) type"
feature = Feature(input=input, transformer=transformer, name=name)
