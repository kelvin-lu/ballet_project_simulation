from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Kitchen Qual"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Kitchen quality type"
feature = Feature(input=input, transformer=transformer, name=name)
