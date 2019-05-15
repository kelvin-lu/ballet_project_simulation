from ballet import Feature
import ballet.eng


def is_partial_sale(ser):
    return (ser == "Partial").astype(int)


input = "Sale Condition"
transformer = ballet.eng.SimpleFunctionTransformer(is_partial_sale)
name = "Is sale of partially completed home"
feature = Feature(input=input, transformer=transformer, name=name)
