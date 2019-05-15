from ballet import Feature
import ballet.eng

input = ["Garage Area"]

transformer = ballet.eng.missing.NullFiller()

name = "Garage area"

feature = Feature(input=input, transformer=transformer, name=name)
