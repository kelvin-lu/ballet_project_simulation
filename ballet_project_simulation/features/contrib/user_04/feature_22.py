from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Functional"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="Typ"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Home functionality type"
feature = Feature(input=input, transformer=transformer, name=name)
