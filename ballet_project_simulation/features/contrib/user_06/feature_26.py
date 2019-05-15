from ballet import Feature
import ballet.eng


def has_contour(ser):
    return (ser == "Lvl").astype(int)


input = "Land Contour"
transformer = ballet.eng.SimpleFunctionTransformer(has_contour)
name = "Property is near flat/level"
feature = Feature(input=input, transformer=transformer, name=name)
