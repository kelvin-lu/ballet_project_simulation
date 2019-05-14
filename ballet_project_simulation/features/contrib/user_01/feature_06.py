from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Utilities"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Utilities type"
feature = Feature(input=input, transformer=transformer, name=name)
