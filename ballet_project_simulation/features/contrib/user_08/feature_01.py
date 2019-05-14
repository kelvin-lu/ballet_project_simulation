import numpy as np
from ballet import Feature
from ballet.eng import SimpleFunctionTransformer

input = "Lot Area"
transformer = SimpleFunctionTransformer(np.sqrt)
name = "Sqrt Lot Area"
feature = Feature(input=input, transformer=transformer, name=name)
