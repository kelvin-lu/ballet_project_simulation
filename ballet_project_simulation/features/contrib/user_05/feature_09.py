from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Bsmt Qual"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="NoBsmt"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Height of the basement type"
feature = Feature(input=input, transformer=transformer, name=name)
