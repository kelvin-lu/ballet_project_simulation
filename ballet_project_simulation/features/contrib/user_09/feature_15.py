from ballet import Feature
import ballet.eng


input = "Total Bsmt SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 3057.0) & (ser <= 3566.5)).astype(int)
)
name = "Total basement square feet group 7"
feature = Feature(input=input, transformer=transformer, name=name)
