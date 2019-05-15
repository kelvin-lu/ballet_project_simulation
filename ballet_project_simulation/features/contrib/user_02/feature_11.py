from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Condition 1"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Proximity to various conditions"
feature = Feature(input=input, transformer=transformer, name=name)
