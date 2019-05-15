from ballet import Feature
import ballet.eng
import sklearn.preprocessing

input = ["Garage Qual"]

transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]

name = "Garage quality type"

feature = Feature(input=input, transformer=transformer, name=name)
