from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Garage Cond"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Garage Cond type"
feature = Feature(input=input, transformer=transformer, name=name)
