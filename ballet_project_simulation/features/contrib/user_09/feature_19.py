from ballet import Feature
import ballet.eng


input = "1st Flr SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 1921.0) & (ser <= 2714.5)).astype(int)
)
name = "First floor square feet group 3"
feature = Feature(input=input, transformer=transformer, name=name)
