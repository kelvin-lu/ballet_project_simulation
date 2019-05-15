from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["House Style"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Style of dwelling"
feature = Feature(input=input, transformer=transformer, name=name)
