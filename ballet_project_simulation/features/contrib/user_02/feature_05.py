from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Foundation"]
transformer = [
    ballet.eng.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Foundation Type"
feature = Feature(input=input, transformer=transformer, name=name)
