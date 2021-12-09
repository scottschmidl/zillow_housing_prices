from env import username, password, hostname
from sklearn.model_selection import train_test_split
import pandas as pd
from scipy import stats
import numpy as np

class Wrangle:

    @classmethod
    def __get_connection(cls, db, user=username, password=password, host=hostname):
        """get_connection: connects to mysql database

        Args:
            db (string): db to connect
            user (string, optional): name of user with which to login. Defaults to un.
            password (string, optional): password of user with which to login. Defaults to pw.
            host (string, optional): host name to connect. Defaults to hn.

        Returns:
            [string]: [string used to connect to mysql]
        """
        return f'mysql+pymysql://{user}:{password}@{host}/{db}'

    @classmethod
    def __get_zillow_data(cls):
        """__get_zillow_data: get data from csv or mysql

        Returns:
            pandas dataframe: used for analysis and modeling
        """
        filename = "zillow.csv"
        db = "zillow"

        try:
            df = pd.read_csv(filename)

        except:
            print(f"{filename} not found. Connecting to MySQL database and reading table to dataframe.")

            # read the SQL query into a dataframe
            query = """SELECT bedroomcnt, bathroomcnt, calculatedfinishedsquarefeet, taxvaluedollarcnt,
                                yearbuilt, taxamount, fips
                    FROM propertylandusetype
                    JOIN properties_2017 USING(propertylandusetypeid)
                    WHERE propertylandusedesc in ('Single Family Residential', 'Inferred Single Family Residential')"""

            df = pd.read_sql(query, Wrangle.__get_connection(db))
            print("Connected successfully")

            # Cache the data for later
            df.to_csv(filename, index=False)
            print(f"Table saved to {filename}")

        finally:
            return df

    @classmethod
    def __clean_zillow(cls):
        """clean_zillow: clean the data to use for vizualization and modeling

        Returns:
            pandas dataframe: used for analysis and modeling
        """

        # call the data
        zillow = Wrangle.__get_zillow_data()

        # rename columns for reability
        cols_rename = {"bedroomcnt": "bedroom_count", "bathroomcnt": "bathroom_count", "calculatedfinishedsquarefeet": "calculated_finished_sq_ft", "taxvaluedollarcnt": "tax_value_dollar_count", "yearbuilt": "year_built"}
        zillow.rename(cols_rename, axis=1, inplace=True)

        # drop na's and reset index
        zillow.dropna(inplace=True)
        zillow.reset_index(inplace=True, drop=True)

        # drop rows where bathrooms are 0
        zillow.drop(zillow[zillow["bathroom_count"] == 0].index, axis=0, inplace=True)

        # remove outliers that are outside of 3 standard deviations
        zillow = zillow[(np.abs(stats.zscore(zillow)) < 3).all(axis=1)]

        # remove tax amount due to leakage
        zillow.drop(columns="taxamount", axis=1, inplace=True)

        return zillow

    def wrangle_zillow(self):
        """wrangle_zillow: split the dataframe into three subsets

        Returns:
            tuple: three subset dataframes split for visualtion and modeling
        """
        df = Wrangle.__clean_zillow()
        train, test = train_test_split(df, test_size=.2, random_state=123)
        train, val = train_test_split(train, test_size=.2, random_state=123)

        return train, val, test

def main():
    pass

if __name__ == "__main__":
    main()