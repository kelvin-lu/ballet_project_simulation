from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Bsmt Qual"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Bsmt Qual type"
feature = Feature(input=input, transformer=transformer, name=name)
