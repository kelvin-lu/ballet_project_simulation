from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Bsmt Cond"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Basement condition type"
feature = Feature(input=input, transformer=transformer, name=name)
