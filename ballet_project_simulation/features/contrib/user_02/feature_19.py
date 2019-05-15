from ballet import Feature
import ballet.eng


def order_fireplace_quality(ser):
    return ser.map({"None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5})


input = "Fireplace Qu"
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    ballet.eng.SimpleFunctionTransformer(order_fireplace_quality),
]
name = "Ordered fireplace quality"
feature = Feature(input=input, transformer=transformer, name=name)
