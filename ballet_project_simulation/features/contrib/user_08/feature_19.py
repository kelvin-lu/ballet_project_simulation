from ballet import Feature
import ballet.eng
import sklearn.preprocessing

input = ["Fence"]

transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]

name = "Fence type"

misc_fill = Feature(input=input, transformer=transformer, name=name)
