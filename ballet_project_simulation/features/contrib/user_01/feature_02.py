from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Street"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Street type"
feature = Feature(input=input, transformer=transformer, name=name)
