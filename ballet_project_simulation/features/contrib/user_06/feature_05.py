from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Garage Qual"]
transformer = [NullFiller(replacement="Missing"), OneHotEncoder()]
name = "Garage qualty fill"
feature = Feature(input=input, transformer=transformer, name=name)
