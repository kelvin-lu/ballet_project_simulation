from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Garage Finish"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Garage Finish type"
feature = Feature(input=input, transformer=transformer, name=name)
