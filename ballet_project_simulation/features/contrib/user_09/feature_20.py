from ballet import Feature
import ballet.eng


input = "1st Flr SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 2714.5) & (ser <= 3508.0)).astype(int)
)
name = "First floor square feet group 4"
feature = Feature(input=input, transformer=transformer, name=name)
