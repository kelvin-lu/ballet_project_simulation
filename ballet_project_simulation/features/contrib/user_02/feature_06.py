from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Roof Style"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Type of roof"
feature = Feature(input=input, transformer=transformer, name=name)
