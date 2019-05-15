from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "Lot Area"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("Lot Area".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "Lot Area unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
