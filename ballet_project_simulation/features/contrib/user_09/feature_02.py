from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Bsmt Qual"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Basement height type"
feature = Feature(input=input, transformer=transformer, name=name)
