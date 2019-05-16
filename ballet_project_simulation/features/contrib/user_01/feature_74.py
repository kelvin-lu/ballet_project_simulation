from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "Open Porch SF"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("Open Porch SF".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "Open Porch SF unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
