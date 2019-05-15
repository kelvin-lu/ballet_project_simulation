from ballet import Feature
import ballet.eng


input = "3Ssn Porch"
transformer = ballet.eng.SimpleFunctionTransformer(lambda ser: ser > 0)
name = "Has three-season porch"
feature = Feature(input=input, transformer=transformer, name=name)
