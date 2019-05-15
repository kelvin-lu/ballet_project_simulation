from ballet import Feature
import ballet.eng


input = "Garage Cond"
order = {"None": 0, "Po": 1, "Fa": 2, "TA": 3, "Gd": 4, "Ex": 5}
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    ballet.eng.SimpleFunctionTransformer(lambda ser: ser.map(order)),
]
name = "Garage condition ordered"
feature = Feature(input=input, transformer=transformer, name=name)
