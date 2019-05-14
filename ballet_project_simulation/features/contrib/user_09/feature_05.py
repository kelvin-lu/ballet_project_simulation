from ballet import Feature
from ballet.eng import SimpleFunctionTransformer

input = "BsmtFin SF 2"


def has_qual(ser):
    return (ser > 0).astype(int)


transformer = SimpleFunctionTransformer(has_qual)
name = "Basement type 2 indicator"
feature = Feature(input=input, transformer=transformer, name=name)
