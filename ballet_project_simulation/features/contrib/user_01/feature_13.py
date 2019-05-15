from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["House Style"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "House Style type"
feature = Feature(input=input, transformer=transformer, name=name)
