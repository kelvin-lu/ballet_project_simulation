from ballet import Feature
import ballet.eng


input = ["Mas Vnr Area"]
transformer = ballet.eng.missing.NullFiller()
name = "Masonry veneer area"
feature = Feature(input=input, transformer=transformer, name=name)
