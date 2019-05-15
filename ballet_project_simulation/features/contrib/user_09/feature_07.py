from ballet import Feature
import ballet.eng


input = "Bsmt Unf SF"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: ((ser > 778.667) & (ser <= 1557.333)).astype(int)
)
name = "Unfinished square feet of basement group 2"
feature = Feature(input=input, transformer=transformer, name=name)
