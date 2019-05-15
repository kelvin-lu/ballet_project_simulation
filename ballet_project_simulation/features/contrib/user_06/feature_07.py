from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Garage Cars"]
transformer = [ballet.eng.missing.NullFiller(), sklearn.preprocessing.OneHotEncoder()]
name = "Size of garages in cars type"
feature = Feature(input=input, transformer=transformer, name=name)
