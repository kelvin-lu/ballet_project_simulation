from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Exterior 2nd"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Exterior 2nd type"
feature = Feature(input=input, transformer=transformer, name=name)
