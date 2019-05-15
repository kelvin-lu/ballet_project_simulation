from ballet import Feature
import ballet.eng


def has_paved_driveway(ser):
    return (ser == "Y").astype(int)


input = "Paved Drive"
transformer = ballet.eng.SimpleFunctionTransformer(has_paved_driveway)
name = "Has paved driveway"
feature = Feature(input=input, transformer=transformer, name=name)
