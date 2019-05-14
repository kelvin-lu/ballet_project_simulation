from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["BsmtFin Type 2"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Rating of basement finished area (if multiple types)"
feature = Feature(input=input, transformer=transformer, name=name)
