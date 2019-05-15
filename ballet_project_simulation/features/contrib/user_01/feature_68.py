from ballet import Feature
import ballet.eng
import numpy as np
import sklearn.impute


input = "TotRms AbvGrd"
transformer = [
    ballet.eng.ConditionalTransformer(
        lambda ser: ser.skew() > 0.75, lambda ser: np.log1p(ser)
    ),
    ballet.eng.NamedFramer("TotRms AbvGrd".replace(" ", "")),
    sklearn.impute.SimpleImputer(strategy="mean"),
]
name = "TotRms AbvGrd unskewed"
feature = Feature(input=input, transformer=transformer, name=name)
