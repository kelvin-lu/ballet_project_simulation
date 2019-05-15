from ballet import Feature
import ballet.eng


input = "Total Bsmt SF"
transformer = ballet.eng.missing.NullFiller()
name = "Total square feet of basement area"
feature = Feature(input=input, transformer=transformer, name=name)
