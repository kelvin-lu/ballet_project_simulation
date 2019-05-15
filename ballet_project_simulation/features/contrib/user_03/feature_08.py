from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Bsmt Cond"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "General condition of basement type"
feature = Feature(input=input, transformer=transformer, name=name)
