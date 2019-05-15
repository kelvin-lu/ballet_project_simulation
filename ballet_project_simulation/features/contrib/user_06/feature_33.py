from ballet import Feature
import ballet.eng


def in_neighborhood_custom(ser):
    return ser.isin(
        ["Crawfor", "Somerst, Timber", "StoneBr", "NoRidge", "NridgeHt"]
    ).astype(int)


input = "Neighborhood"
transformer = ballet.eng.SimpleFunctionTransformer(in_neighborhood_custom)
name = "Is in custom 6 neighborhood group"
feature = Feature(input=input, transformer=transformer, name=name)
