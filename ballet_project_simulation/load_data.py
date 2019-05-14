import pandas as pd

from ballet.util.io import load_table_from_config
from funcy import some, where

from ballet_project_simulation import conf


def load_data(input_dir=None):
    """Load data"""
    if input_dir is not None:
        tables = conf.get("tables")

        entities_table_name = conf.get("data", "entities_table_name")
        entities_config = some(where(tables, name=entities_table_name))
        X_df = load_table_from_config(input_dir, entities_config)

        targets_table_name = conf.get("data", "targets_table_name")
        targets_config = some(where(tables, name=targets_table_name))
        y_df = load_table_from_config(input_dir, targets_config)
    else:
        source = "https://s3.amazonaws.com/mit-dai-ballet/ames/AmesHousing.txt"
        df = pd.read_csv(source, sep="\t")
        X_df = df.drop("SalePrice", axis=1)
        y_df = df["SalePrice"]

    return X_df, y_df

