from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Mas Vnr Area"]
transformer = [ballet.eng.missing.NullFiller(), sklearn.preprocessing.OneHotEncoder()]
name = "Masonry veneer area in square feet type"
feature = Feature(input=input, transformer=transformer, name=name)
