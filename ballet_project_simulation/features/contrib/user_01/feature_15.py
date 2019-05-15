from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Roof Matl"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Roof Matl type"
feature = Feature(input=input, transformer=transformer, name=name)
