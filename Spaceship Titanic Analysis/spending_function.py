def encode_spending(df, columns):
    """
    Encodes spending-related columns in the DataFrame by creating binary
    categorical variables.

    For each column in the provided list of `columns`, this function
    creates a new binary feature that indicates whether the spending in that
    column is greater than 0. A value of 1 represents any non-zero spending
    (indicating the passenger used that service), and a value of 0 represents
    zero spending (indicating the passenger did not use that service).

    Args:
        df (pandas.DataFrame): The input DataFrame containing passenger data.
        columns (list of str): A list of column names in the DataFrame
                                representing various services
                                (e.g., RoomService, FoodCourt, etc.)
                                that have spending values.

    Returns:
        pandas.DataFrame: The DataFrame with new binary columns added for each
        of the input `columns`. Each new column is named in the format
        "{col}_cat", where `col` is the original column name, representing
        whether the spending was greater than zero.
    """
    for col in columns:
        df[f"{col}_cat"] = (df[col] > 0).astype(int)
    return df
