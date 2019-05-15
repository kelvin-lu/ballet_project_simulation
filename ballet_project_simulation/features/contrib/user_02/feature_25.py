from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["MS SubClass"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Type of dwelling involved in the sale"
feature = Feature(input=input, transformer=transformer, name=name)
