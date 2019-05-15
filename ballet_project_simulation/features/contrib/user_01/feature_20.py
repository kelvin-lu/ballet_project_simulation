from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Exter Cond"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Exter Cond type"
feature = Feature(input=input, transformer=transformer, name=name)
