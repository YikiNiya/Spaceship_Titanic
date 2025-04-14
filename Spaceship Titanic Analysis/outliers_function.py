def outliers(df, column):
    """
    Identifies outliers in a specified column of a DataFrame using
    the IQR method.

    This function calculates the Interquartile Range (IQR) for the specified
    column of the DataFrame and determines outliers based on the 1.5 * IQR
    rule. Any values outside the lower and upper bounds are considered
    outliers.

    Args:
        df (pandas.DataFrame): The DataFrame containing the data.
        column (str): The name of the column in which to identify outliers.

    Returns:
        pandas.Series: A binary series (0 or 1) indicating whether the
        corresponding value in the column is an outlier
        (1 for outliers, 0 for non-outliers).
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return ((df[column] < lower_bound) | (df[column] > upper_bound)).astype(
        int
    )  # noqa: E501
