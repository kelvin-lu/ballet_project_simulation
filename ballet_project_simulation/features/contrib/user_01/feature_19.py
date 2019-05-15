from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Exter Qual"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Exter Qual type"
feature = Feature(input=input, transformer=transformer, name=name)
