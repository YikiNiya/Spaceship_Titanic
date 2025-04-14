import pandas as pd


def process_cabin(df):
    """
    Processes the 'Cabin' column only if it exists.

    Processes the 'Cabin' column by:
    - Filling missing values with 'Unknown/0/Unknown'
    - Splitting it into 'Deck', 'Number', and 'Side'
    - Converting 'Number' to numeric
    - Dropping the original 'Cabin' column

    Args:
        X (pd.DataFrame): Input DataFrame

    Returns:
        pd.DataFrame: Processed DataFrame
    """
    if "Cabin" not in df.columns:
        return df

    df["Cabin"] = df["Cabin"].fillna("Unknown/0/Unknown")
    df[["Deck", "Number", "Side"]] = df["Cabin"].str.split("/", expand=True)
    df["Number"] = pd.to_numeric(df["Number"], errors="coerce").fillna(0)
    df.drop(columns=["Cabin"], inplace=True)

    return df
