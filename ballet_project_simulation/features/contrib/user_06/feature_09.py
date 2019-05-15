from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Garage Type"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="missing"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Garage type"
feature = Feature(input=input, transformer=transformer, name=name)
