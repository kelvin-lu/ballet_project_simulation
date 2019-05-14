from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Land Contour"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Land Contour type"
feature = Feature(input=input, transformer=transformer, name=name)
