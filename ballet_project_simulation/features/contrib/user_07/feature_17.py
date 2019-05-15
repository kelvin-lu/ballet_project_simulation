from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Land Contour"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Flatness of the property type"
misc_fill = Feature(input=input, transformer=transformer)
