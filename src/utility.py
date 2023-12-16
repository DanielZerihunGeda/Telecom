import pandas as pd
from sqlalchemy import create_engine

class DataProcessor:
    def __init__(self, username, password, host, database, table_name):
        self.username = username
        self.password = password
        self.host = host
        self.database = database
        self.table_name = table_name
        self.df = None  # Initialize df attribute

    def fetch_data(self):
        connection_str = f"postgresql+psycopg2://{self.username}:{self.password}@{self.host}/{self.database}"
        engine = create_engine(connection_str)

        query = f"SELECT * FROM {self.table_name}"

        self.df = pd.read_sql_query(query, engine)
        
        engine.dispose()
        return self.df  # Return the DataFrame after fetching data

    def drop_null_rows(self, column):
        if self.df is not None and column in self.df.columns:
            self.df.dropna(subset=[column], inplace=True)
        return self.df  # Return the DataFrame after dropping null rows
    
    def drop_columns(self, columns_to_drop):
        if self.df is not None:
            self.df.drop(columns=columns_to_drop, inplace=True, errors='ignore')
        return self.df #Return the DataFrame after dropping column

    def assign_zero_based_on_condition(self, related_cols, target_cols):
        if self.df is not None:
            mask = self.df[target_cols].isnull().any(axis=1)
            for idx, row in self.df.iterrows():
                if any(pd.isnull(row[col]) for col in target_cols) and any(row[col] != 0 for col in related_cols):
                    for col in target_cols:
                        self.df.at[idx, col] = 0
        return self.df  
