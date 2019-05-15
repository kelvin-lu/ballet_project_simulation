from ballet import Feature
import ballet.eng


def has_standard_electrical(ser):
    return (ser == "SBrkr").astype(int)


input = "Electrical"
transformer = ballet.eng.SimpleFunctionTransformer(has_standard_electrical)
name = "Has standard electrical system"
feature = Feature(input=input, transformer=transformer, name=name)
