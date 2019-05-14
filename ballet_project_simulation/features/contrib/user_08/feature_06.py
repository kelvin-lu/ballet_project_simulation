from ballet import Feature
import ballet.eng
import sklearn.preprocessing

input = ["Alley"]

transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]

name = "Alley Type"
feature = Feature(input=input, transformer=transformer, name=name)
