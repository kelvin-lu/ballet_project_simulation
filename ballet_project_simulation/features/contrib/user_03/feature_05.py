from ballet import Feature
from ballet.eng import NullFiller, SimpleFunctionTransformer


input = ["Full Bath", "Half Bath", "Bsmt Full Bath", "Bsmt Half Bath"]
transformer = [SimpleFunctionTransformer(lambda df: df.sum(axis=1)), NullFiller()]
name = "Bathroom Count"
feature = Feature(input=input, transformer=transformer, name=name)
