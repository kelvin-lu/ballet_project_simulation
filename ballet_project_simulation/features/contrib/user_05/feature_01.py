from ballet import Feature
import ballet.eng
import sklearn.preprocessing

input = ["Alley"]
transformer = [
    ballet.eng.NullFiller(replacement="NOACCESS"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Alley Misc Fill"
feature = Feature(input=input, transformer=transformer, name=name)
