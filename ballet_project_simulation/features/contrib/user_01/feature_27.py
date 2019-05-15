from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Heating"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Heating type"
feature = Feature(input=input, transformer=transformer, name=name)
