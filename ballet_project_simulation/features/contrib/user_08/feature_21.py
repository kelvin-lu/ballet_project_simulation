from ballet import Feature
import ballet.eng


def has_qual(ser):

    return (ser > 1).astype(int)


input = "Fireplaces"

transformer = ballet.eng.SimpleFunctionTransformer(func=has_qual)

name = "Has more than one fireplace"

feature = Feature(input=input, transformer=transformer, name=name)
