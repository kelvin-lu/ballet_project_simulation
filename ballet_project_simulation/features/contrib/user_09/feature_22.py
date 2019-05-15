from ballet import Feature
import ballet.eng


input = "1st Flr SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: (ser > 4301.5).astype(int)
)
name = "First floor square feet group 6"
feature = Feature(input=input, transformer=transformer, name=name)
