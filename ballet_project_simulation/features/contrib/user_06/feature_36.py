from ballet import Feature
import ballet.eng


def calc_age(ser):
    return 2018 - ser


input = "Year Built"
transformer = ballet.eng.SimpleFunctionTransformer(calc_age)
name = "Age of house since built"
feature = Feature(input=input, transformer=transformer, name=name)
