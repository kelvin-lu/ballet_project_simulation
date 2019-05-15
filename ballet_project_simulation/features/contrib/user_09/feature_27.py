from ballet import Feature
import ballet.eng


input = "2nd Flr SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 1241.333) & (ser <= 1551.667)).astype(int)
)
name = "Second floor square feet group 5"
feature = Feature(input=input, transformer=transformer, name=name)
