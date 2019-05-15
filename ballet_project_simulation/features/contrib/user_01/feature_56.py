from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "Bsmt Unf SF"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("Bsmt Unf SF".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "Bsmt Unf SF unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
