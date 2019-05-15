from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Functional"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Functional type"
feature = Feature(input=input, transformer=transformer, name=name)
