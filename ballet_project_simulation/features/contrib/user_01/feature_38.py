from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Paved Drive"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Paved Drive type"
feature = Feature(input=input, transformer=transformer, name=name)
