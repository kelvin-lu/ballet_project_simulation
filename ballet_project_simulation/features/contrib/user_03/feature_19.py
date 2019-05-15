from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Fence"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Fence type"
feature = Feature(input=input, transformer=transformer, name=name)
