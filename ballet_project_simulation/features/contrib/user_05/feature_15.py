from ballet import Feature
import ballet.eng
import numpy as np


# this is the author's feature, but the input does not exist. replacing with
# zeros.

# input = ["Kitchen AbvGr"]
# transformer = [
#     ballet.eng.missing.NullFiller(replacement="missing"),
#     sklearn.preprocessing.OneHotEncoder(),
# ]

input = "Alley"
transformer = ballet.eng.SimpleFunctionTransformer(
    lambda ser: np.zeros((ser.shape[0], 1))
)
name = "Zeros"
feature = Feature(input=input, transformer=transformer, name=name)
