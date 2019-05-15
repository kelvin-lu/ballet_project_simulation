from ballet import Feature
import ballet.eng


input = "Total Bsmt SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 509.5) & (ser <= 1019.0)).astype(int)
)
name = "Total basement square feet group 2"
feature = Feature(input=input, transformer=transformer, name=name)
