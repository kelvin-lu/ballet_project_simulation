from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Foundation"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Foundation type"
feature = Feature(input=input, transformer=transformer, name=name)
