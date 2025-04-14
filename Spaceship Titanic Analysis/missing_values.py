def num_imputation(df):
    """
    Imputes missing values in numerical columns.

    - Fills missing values in the 'Age' column with the median.

    Args:
        X (pd.DataFrame): The input DataFrame.

    Returns:
        pd.DataFrame: The DataFrame with missing values in 'Age' imputed.
    """
    df["Age"] = df["Age"].fillna(df["Age"].median())

    return df
