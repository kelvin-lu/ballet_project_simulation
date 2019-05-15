from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Sale Condition"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Sale Condition type"
feature = Feature(input=input, transformer=transformer, name=name)
