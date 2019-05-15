from ballet import Feature
import ballet.eng


input = ["Pool QC"]

transformer = [
    ballet.eng.NullIndicator(),
    ballet.eng.SimpleFunctionTransformer(lambda x: ~x),
]

name = "Whether pool quality is non-missing"

feature = Feature(input=input, transformer=transformer, name=name)
