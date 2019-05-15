from ballet import Feature
import ballet.eng
import sklearn.preprocessing

input = ["Fireplace Qu"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Fireplace quality type"
feature = Feature(input=input, transformer=transformer, name=name)
