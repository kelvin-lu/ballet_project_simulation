from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Land Slope"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Land Slope type"
feature = Feature(input=input, transformer=transformer, name=name)
