from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["MS Zoning"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "MS Zoning type"
feature = Feature(input=input, transformer=transformer, name=name)
