from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "Screen Porch"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("Screen Porch".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "Screen Porch unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
