from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Sale Condition"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="missing"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Condition of sale type"
feature = Feature(input=input, transformer=transformer, name=name)
