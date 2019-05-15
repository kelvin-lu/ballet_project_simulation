from ballet import Feature
import ballet.eng


input = "Total Bsmt SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 1528.5) & (ser <= 2038.0)).astype(int)
)
name = "Total basement square feet group 4"
feature = Feature(input=input, transformer=transformer, name=name)
