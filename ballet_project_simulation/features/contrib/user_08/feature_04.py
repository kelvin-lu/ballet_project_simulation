from ballet import Feature
from ballet.eng import NullFiller

input = "Mas Vnr Area"
transformer = NullFiller()
name = "Masonry Veneer Area Fill"
feature = Feature(input=input, transformer=transformer, name=name)
