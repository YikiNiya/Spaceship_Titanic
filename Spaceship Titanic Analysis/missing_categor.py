def fill_categorical_missing(df, columns):
    """
    Fills missing values in categorical columns with 'Unknown'.

    Args:
        X (pd.DataFrame): The input DataFrame.
        columns (list): List of categorical columns to process.

    Returns:
        pd.DataFrame: Updated DataFrame with missing values filled.
    """
    for col in columns:
        df[col] = df[col].fillna("Unknown")
    return df
