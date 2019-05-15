from ballet import Feature
import ballet.eng


def has_qual(ser):

    return (ser == "TenC").astype(int)


input = "Misc Feature"

transformer = ballet.eng.SimpleFunctionTransformer(func=has_qual)

name = "Has miscellaneous feature: tennis court"

feature = Feature(input=input, transformer=transformer, name=name)
