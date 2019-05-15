from ballet import Feature
import ballet.eng


input = "Total Bsmt SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 1019.0) & (ser <= 1528.5)).astype(int)
)
name = "Total basement square feet group 3"
feature = Feature(input=input, transformer=transformer, name=name)
