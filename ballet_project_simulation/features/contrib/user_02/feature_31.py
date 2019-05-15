from ballet import Feature
import ballet.eng


input = ["Gr Liv Area", "Total Bsmt SF"]
transformer = ballet.eng.SimpleFunctionTransformer(lambda df: df.sum(axis=1))
name = "Total area"
feature = Feature(input=input, transformer=transformer, name=name)
