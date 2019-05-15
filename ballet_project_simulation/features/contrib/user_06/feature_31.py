from ballet import Feature
import ballet.eng


def has_wood_deck(ser):
    return (ser > 0).astype(int)


input = ["Wood Deck SF"]
transformer = ballet.eng.SimpleFunctionTransformer(has_wood_deck)
name = "Has wood deck"
feature = Feature(input=input, transformer=transformer, name=name)
