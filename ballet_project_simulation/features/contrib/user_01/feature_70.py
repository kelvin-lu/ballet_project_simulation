from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "Garage Yr Blt"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("Garage Yr Blt".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "Garage Yr Blt unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
