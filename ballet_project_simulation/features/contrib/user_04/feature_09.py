from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Land Slope"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Slope of property type"
feature = Feature(input=input, transformer=transformer, name=name)
