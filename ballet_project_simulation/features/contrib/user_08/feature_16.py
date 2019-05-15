from ballet import Feature
import ballet.eng

input = ["Garage Cars"]

transformer = ballet.eng.missing.NullFiller(isnull=pd.isnull)

misc_fill = Feature(input=input, transformer=transformer)
