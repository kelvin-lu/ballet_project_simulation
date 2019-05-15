from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Utilities"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="missing"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Type of utilities available"
feature = Feature(input=input, transformer=transformer, name=name)
