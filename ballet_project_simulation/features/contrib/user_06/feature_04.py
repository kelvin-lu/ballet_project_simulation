from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Garage Finish"]
transformer = [NullFiller(replacement="Missing"), OneHotEncoder()]
name = "Garage finish fill"
feature = Feature(input=input, transformer=transformer, name=name)
