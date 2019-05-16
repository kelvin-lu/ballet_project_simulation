from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "Enclosed Porch"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("Enclosed Porch".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "Enclosed Porch unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
