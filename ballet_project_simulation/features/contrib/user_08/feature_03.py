from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Mas Vnr Type"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Masonry Veneer Types"
feature = Feature(input=input, transformer=transformer)
