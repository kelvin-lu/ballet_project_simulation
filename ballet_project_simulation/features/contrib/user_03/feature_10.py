from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Bsmt Exposure"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Basement walkout or garden level walls type"
feature = Feature(input=input, transformer=transformer, name=name)
