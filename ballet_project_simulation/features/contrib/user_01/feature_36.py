from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Garage Qual"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Garage Qual type"
feature = Feature(input=input, transformer=transformer, name=name)
