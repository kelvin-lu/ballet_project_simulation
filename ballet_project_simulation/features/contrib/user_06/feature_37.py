from ballet import Feature
import ballet.eng


def calc_age(ser):
    return 2018 - ser


input = "Yr Sold"
transformer = ballet.eng.SimpleFunctionTransformer(calc_age)
name = "Years since sold"
feature = Feature(input=input, transformer=transformer, name=name)
