import pandas as pd
import numpy as np


def extract_group_features(df):
    """
    Extracts group features from 'PassengerId' and 'Name' columns and creates
    new features: 'GroupID', 'GroupSize', 'Surname', 'FamilySize', and
    'IsSolo'.

    Args:
        df (pd.DataFrame): The input DataFrame with 'PassengerId' and 'Name'
        columns.

    Returns:
        pd.DataFrame: Updated DataFrame with new features.
    """
    if "Name" not in df.columns:
        return df

    df["GroupID"] = df["PassengerId"].apply(lambda x: x.split("_")[0])
    group_sizes = df["GroupID"].value_counts()
    df["GroupSize"] = df["GroupID"].map(group_sizes)
    df["Surname"] = df["Name"].apply(
        lambda x: (
            x.split()[1] if pd.notnull(x) and len(x.split()) > 1 else np.nan
        )  # noqa: E501
    )
    surname_counts = df["Surname"].value_counts()
    df["FamilySize"] = df["Surname"].map(surname_counts)
    df["FamilySize"] = df["FamilySize"].fillna(df["GroupSize"])
    df["FamilySize"] = df["FamilySize"].fillna(1).astype(int)
    df["IsSolo"] = (df["FamilySize"] == 1).astype(int)

    df.drop(columns=["Name", "Surname"], inplace=True)

    return df
