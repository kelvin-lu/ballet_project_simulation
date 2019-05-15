from ballet import Feature
import ballet.eng


input = "Total Bsmt SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: (ser <= 509.5).astype(int)
)
name = "Total basement square feet group 1"
feature = Feature(input=input, transformer=transformer, name=name)
