from ballet import Feature
import ballet.eng
import sklearn.preprocessing


input = ["Garage Area"]
transformer = [ballet.eng.missing.NullFiller(), sklearn.preprocessing.OneHotEncoder()]
name = "Garage area fill"
feature = Feature(input=input, transformer=transformer, name=name)
