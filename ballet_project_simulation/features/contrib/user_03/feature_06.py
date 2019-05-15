from ballet import Feature
import numpy as np
import ballet.eng


def calc_garage_per_car(df):
    return df["Garage Area"] / df["Garage Cars"]


input = ["Garage Area", "Garage Cars"]
transformer = [
    ballet.eng.SimpleFunctionTransformer(calc_garage_per_car),
    ballet.eng.NullFiller(isnull=np.isinf, replacement=0.0),
    ballet.eng.NullFiller(replacement=0.0),
]
name = "Garage area per car"
feature = Feature(input=input, transformer=transformer, name=name)
