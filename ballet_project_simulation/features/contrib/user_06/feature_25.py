from ballet import Feature
import ballet.eng


def has_reg(ser):
    return (ser == "Reg").astype(int)


input = "Lot Shape"
transformer = ballet.eng.SimpleFunctionTransformer(has_reg)
name = "Has regular lot shape"
feature = Feature(input=input, transformer=transformer, name=name)
