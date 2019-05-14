from ballet import Feature
from ballet.eng import NamedFramer, SimpleFunctionTransformer
from sklearn.preprocessing import OneHotEncoder


# Zeros in 020-090 get cut off. This feature prepends them back.
def pad_zero(ser):
    return ser.astype(str).str.pad(3, side="left", fillchar="0")


input = "MS SubClass"
transformer = [
    SimpleFunctionTransformer(pad_zero),
    NamedFramer("MS SubClass"),
    OneHotEncoder(),
]
name = "Pad zeros in MS SubClass"
feature = Feature(input=input, transformer=transformer, name=name)
