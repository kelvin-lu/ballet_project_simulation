from ballet import Feature
import ballet.eng
import sklearn.preprocessing

input = ["Pool QC"]

transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    sklearn.preprocessing.OneHotEncoder(),
]

name = "Pool quality type"

feature = Feature(input=input, transformer=transformer, name=name)
