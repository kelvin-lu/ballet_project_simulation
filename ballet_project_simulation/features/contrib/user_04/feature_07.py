from ballet import Feature
import ballet.eng


input = "Screen Porch"
transformer = ballet.eng.SimpleFunctionTransformer(lambda ser: ser > 0)
name = "Has screen porch"
feature = Feature(input=input, transformer=transformer, name=name)
