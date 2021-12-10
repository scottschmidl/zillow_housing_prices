from wrangle import Wrangle
from sklearn.preprocessing import MinMaxScaler, StandardScaler, RobustScaler, QuantileTransformer
import pandas as pd

class Prepare:

    def get_Xy(self, train, validate, test):
        """get_Xy [summary]

        Args:
            train ([type]): [description]
            validate ([type]): [description]
            test ([type]): [description]

        Returns:
            [type]: [description]
        """
        X_train = train.drop(["tax_value_dollar_count", "fips", "year_built"], axis=1)
        y_train = train["tax_value_dollar_count"]

        X_val = validate.drop(["tax_value_dollar_count", "fips", "year_built"], axis=1)
        y_val = validate["tax_value_dollar_count"]

        X_test = test.drop(["tax_value_dollar_count", "fips", "year_built"], axis=1)
        y_test = test["tax_value_dollar_count"]

        return (X_train, y_train), (X_val, y_val), (X_test, y_test)

    def scaling(self, X_train, X_validate, X_test):
        """scaling impliments scaling to data

        Args:
            train (pd dataframe): data to fit and transform
            validate (pd dataframe): data to transform
            test (pd dataframe): data to transform
            scale (class): which scaler to use

        Returns:
            np array: scaled data
        """
        scale = StandardScaler()
        scale.fit(X_train)

        X_train_scaled = pd.DataFrame(data=scale.transform(X_train), columns=X_train.columns)
        X_val_scaled = pd.DataFrame(data=scale.transform(X_validate), columns=X_train.columns)
        X_test_scaled = pd.DataFrame(data=scale.transform(X_test), columns=X_train.columns)

        return X_train_scaled, X_val_scaled, X_test_scaled, scale

    def reverse_scaling(X_train_scaled, X_validate_scaled, X_test_scaled, cols, scale):
        """reverse_scaling impliments reverse scaling

        Args:
            train_scaled ([type]): [description]
            validate_scaled ([type]): [description]
            test_scaled ([type]): [description]
            scale ([type]): [description]

        Returns:
            [type]: [description]
        """
        X_train = pd.DataFrame(data=scale.inverse_transform(X_train_scaled), columns=cols)
        X_val = pd.DataFrame(data=scale.inverse_transform(X_validate_scaled), columns=cols)
        X_test = pd.DataFrame(data=scale.inverse_transform(X_test_scaled), columns=cols)

        return X_train, X_val, X_test

def main():
    pass

if __name__ == "__main__":
    main()