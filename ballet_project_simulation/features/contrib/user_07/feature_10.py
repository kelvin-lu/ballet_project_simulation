from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Land Slope"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Slope of property type"
misc_fill = Feature(input=input, transformer=transformer)
