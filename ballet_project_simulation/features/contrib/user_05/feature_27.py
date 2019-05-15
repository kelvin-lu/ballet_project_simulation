from ballet import Feature
import ballet.eng


input = ["Total Bsmt SF", "1st Flr SF", "2nd Flr SF"]
transformer = [
    ballet.eng.SimpleFunctionTransformer(lambda df: df.sum(axis=1)),
    ballet.eng.NullFiller(),
]
name = "Total area calculated"
feature = Feature(input=input, transformer=transformer, name=name)
