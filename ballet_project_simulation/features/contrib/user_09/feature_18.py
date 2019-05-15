from ballet import Feature
import ballet.eng


input = "1st Flr SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 1127.5) & (ser <= 1921.0)).astype(int)
)
name = "First floor square feet group 2"
feature = Feature(input=input, transformer=transformer, name=name)
