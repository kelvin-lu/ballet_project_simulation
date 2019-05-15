from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "Gr Liv Area"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("Gr Liv Area".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "Gr Liv Area unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
