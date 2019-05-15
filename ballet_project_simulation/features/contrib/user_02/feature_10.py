from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Neighborhood"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Neighborhood"
feature = Feature(input=input, transformer=transformer, name=name)
