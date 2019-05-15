from ballet import Feature
import ballet.eng


input = "1st Flr SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: (ser <= 1127.5).astype(int)
)
name = "First floor square feet group 1"
feature = Feature(input=input, transformer=transformer, name=name)
