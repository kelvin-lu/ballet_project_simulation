from ballet import Feature
import ballet.eng


input = "Total Bsmt SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 2038.0) & (ser <= 2547.5)).astype(int)
)
name = "Total basement square feet group 5"
feature = Feature(input=input, transformer=transformer, name=name)
