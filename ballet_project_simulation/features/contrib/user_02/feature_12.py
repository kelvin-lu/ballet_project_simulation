from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Condition 2"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Proximity to various conditions (if more than one is present)"
feature = Feature(input=input, transformer=transformer, name=name)
