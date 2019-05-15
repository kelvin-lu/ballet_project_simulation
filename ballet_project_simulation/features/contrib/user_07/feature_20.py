from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Central Air"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Central air conditioning type"
feature = Feature(input=input, transformer=transformer, name=name)
