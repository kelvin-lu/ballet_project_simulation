from ballet import Feature
from ballet.eng import NullFiller
from sklearn.preprocessing import OneHotEncoder

input = ["Pool QC"]
transformer = [NullFiller(replacement="None"), OneHotEncoder()]
name = "Pool quality type"
feature = Feature(input=input, transformer=transformer, name=name)
