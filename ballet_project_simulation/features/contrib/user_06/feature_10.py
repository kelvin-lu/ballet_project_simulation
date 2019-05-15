from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Garage Finish"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="missing"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Interior finish of the garage type"
feature = Feature(input=input, transformer=transformer, name=name)
