from ballet import Feature
import ballet.eng


def has_gentle_slope(ser):
    return (ser == "Gtl").astype(int)


input = "Land Slope"
transformer = ballet.eng.SimpleFunctionTransformer(has_gentle_slope)
name = "Has gentle land slope"
feature = Feature(input=input, transformer=transformer, name=name)
