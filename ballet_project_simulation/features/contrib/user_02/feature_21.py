from ballet import Feature
import ballet.eng


input = "Garage Finish"
order = {"None": 0, "Unf": 1, "RFn": 2, "Fin": 3}
transformer = [
    ballet.eng.missing.NullFiller(replacement="None"),
    ballet.eng.SimpleFunctionTransformer(lambda ser: ser.map(order)),
]
name = "Ordered garage finish"
feature = Feature(input=input, transformer=transformer, name=name)
