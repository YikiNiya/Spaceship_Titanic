def map_binary_columns(df):
    """
    Map boolean values in binary columns to integer values (0 and 1)
    in the DataFrame.

    This function processes specific binary columns in the dataset,
    which contain boolean values (True/False), and maps them to integers
    (1 for True, 0 for False). It also handles missing values by filling
    them with 0.

    The binary columns processed by this function are:
        - "CryoSleep"
        - "VIP"

    The resulting columns will have 0 for False or missing values and 1 for
    True.

    Args:
        df (pandas.DataFrame): The input DataFrame containing the dataset
        with binary columns.

    Returns:
        pandas.DataFrame: The transformed DataFrame with binary columns
        mapped to integer values.

    Example:
        >>> df = pd.DataFrame({"CryoSleep": [True, False, None],
        "VIP": [None, True, False]})
        >>> map_binary_columns(df)
           CryoSleep  VIP
        0          1    0
        1          0    1
        2          0    0
    """
    binary_columns = ["CryoSleep", "VIP"]

    for col in binary_columns:
        df[col] = df[col].map({False: 0, True: 1})
        df[col] = df[col].fillna(0).astype(int)

    return df
