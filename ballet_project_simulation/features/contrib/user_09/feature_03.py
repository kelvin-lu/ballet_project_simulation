from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["BsmtFin Type 1"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Rating of basement finished area type"
feature = Feature(input=input, transformer=transformer, name=name)
