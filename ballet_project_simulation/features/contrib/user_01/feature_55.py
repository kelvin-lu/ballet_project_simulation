from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "BsmtFin SF 2"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("BsmtFin SF 2".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "BsmtFin SF 2 unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
