from sklearn.base import BaseEstimator, TransformerMixin
from spending_function import encode_spending
from binary_mapping import map_binary_columns
from missing_values import num_imputation
from missing_cabin import process_cabin
from missing_categor import fill_categorical_missing
from extracting_features import extract_group_features


class CustomPreprocessor(BaseEstimator, TransformerMixin):
    """
    A custom preprocessor for transforming the Spaceship Titanic dataset.

    This class is designed to preprocess the dataset by performing various
    transformations, such as encoding spending-related features, handling
    missing values, extracting group-related features, and creating new
    service-related features. It integrates multiple steps commonly used
    in data preprocessing pipelines to prepare the dataset for machine
    learning models.

    In particular, it:
    - Encodes spending columns into binary categorical features
    indicating usage of each service.
    - Maps binary columns into a consistent format.
    - Imputes missing numerical values.
    - Processes the 'Cabin' column for further analysis.
    - Fills missing values in categorical columns such as "HomePlanet"
    and "Destination".
    - Extracts group-level features from the dataset.
    - Creates additional features like "ServiceCount" and "UsedAnyService".

    Args:
        None

    Attributes:
        spending_columns (list): A list of column names representing various
        onboard services where passengers can spend money. These columns will
        be encoded into binary features.

    Methods:
        fit(df, y=None):
            This method does not perform any fitting and returns the
            preprocessor instance.

        transform(df):
            Applies a series of preprocessing steps on the input DataFrame:
            1. Encodes spending-related columns using the `encode_spending`
            function.
            2. Maps binary columns using the `map_binary_columns` function.
            3. Imputes missing numerical values using `num_imputation`.
            4. Processes the 'Cabin' column using `process_cabin`.
            5. Fills missing values in categorical columns "HomePlanet" and
            "Destination" using `fill_categorical_missing`.
            6. Extracts group-level features with the `extract_group_features`
            function.
            7. Creates new features: "ServiceCount" (sum of spending columns)
            and "UsedAnyService" (binary indicator if any service was used).

            Args:
                df (pandas.DataFrame): The input DataFrame containing the
                passenger data.

            Returns:
                pandas.DataFrame: The transformed DataFrame with the newly
                engineered features.
    """

    def __init__(self):
        self.spending_columns = [
            "RoomService",
            "FoodCourt",
            "ShoppingMall",
            "Spa",
            "VRDeck",
        ]

    def fit(self, df, y=None):
        return self

    def transform(self, df):
        df = encode_spending(df, self.spending_columns)
        df = map_binary_columns(df)
        df = num_imputation(df)
        df = process_cabin(df)
        df = fill_categorical_missing(df, ["HomePlanet", "Destination"])
        df = extract_group_features(df)
        df["ServiceCount"] = df[self.spending_columns].sum(axis=1)
        df["UsedAnyService"] = (df["ServiceCount"] > 0).astype(int)

        return df
