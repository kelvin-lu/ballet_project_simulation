from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Exterior 1st"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Exterior covering on house type"
feature = Feature(input=input, transformer=transformer, name=name)
