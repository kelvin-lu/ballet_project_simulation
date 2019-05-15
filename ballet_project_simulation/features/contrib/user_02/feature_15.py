from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Misc Feature"]
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]
name = "Miscellaneous feature not covered in other categories type"
feature = Feature(input=input, transformer=transformer, name=name)
