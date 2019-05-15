from ballet import Feature
from ballet.eng import SimpleFunctionTransformer

input = "Enclosed Porch"
transformer = SimpleFunctionTransformer(lambda ser: ser > 0)
name = "Has enclosed porch"
feature = Feature(input=input, transformer=transformer, name=name)
