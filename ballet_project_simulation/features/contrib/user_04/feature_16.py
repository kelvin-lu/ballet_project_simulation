from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Land Contour"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="missing"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Flatness of the property type"
feature = Feature(input=input, transformer=transformer, name=name)
