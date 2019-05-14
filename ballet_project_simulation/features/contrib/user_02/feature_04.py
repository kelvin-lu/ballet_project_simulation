from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Heating"]
transformer = [
    ballet.eng.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Heating Type"
feature = Feature(input=input, transformer=transformer, name=name)
