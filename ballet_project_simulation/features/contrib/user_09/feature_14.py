from ballet import Feature
import ballet.eng


input = "Total Bsmt SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 2547.5) & (ser <= 3057.0)).astype(int)
)
name = "Total basement square feet group 6"
feature = Feature(input=input, transformer=transformer, name=name)
