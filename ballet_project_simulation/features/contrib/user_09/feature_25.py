from ballet import Feature
import ballet.eng


input = "2nd Flr SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 620.667) & (ser <= 931.0)).astype(int)
)
name = "Second floor square feet group 3"
feature = Feature(input=input, transformer=transformer, name=name)
