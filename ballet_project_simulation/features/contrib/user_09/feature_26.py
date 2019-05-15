from ballet import Feature
import ballet.eng


input = "2nd Flr SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 931.0) & (ser <= 1241.333)).astype(int)
)
name = "Second floor square feet group 4"
feature = Feature(input=input, transformer=transformer, name=name)
