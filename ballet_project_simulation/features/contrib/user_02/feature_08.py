from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Bldg Type"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Type of dwelling"
feature = Feature(input=input, transformer=transformer, name=name)
