from ballet import Feature
import ballet.eng
import sklearn.preprocessing

input = ["BsmtFin Type 2"]

transformer = [
    ballet.eng.missing.NullFiller(replacement="missing"),
    sklearn.preprocessing.OneHotEncoder(),
]

name = "Rating of basement finished area (if multiple types)"

feature = Feature(input=input, transformer=transformer, name=name)
