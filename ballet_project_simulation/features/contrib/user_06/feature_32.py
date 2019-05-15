from ballet import Feature
import ballet.eng


def has_masonry_veneer(ser):
    return (ser > 0).astype(int)


input = "Mas Vnr Area"
transformer = ballet.eng.SimpleFunctionTransformer(has_masonry_veneer)
name = "Has masonry veneer"
feature = Feature(input=input, transformer=transformer, name=name)
