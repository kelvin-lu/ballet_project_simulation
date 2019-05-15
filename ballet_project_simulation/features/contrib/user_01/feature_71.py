from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "Garage Cars"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("Garage Cars".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "Garage Cars unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
