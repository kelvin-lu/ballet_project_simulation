from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "3Ssn Porch"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("3Ssn Porch".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "3Ssn Porch unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
