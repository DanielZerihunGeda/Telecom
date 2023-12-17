from scipy.interpolate import interp1d
import numpy as np
from utility import DataProcessor

class ProcessData:
    # ... (existing code remains unchanged) ...

    def interpolate_nonlinear(self, processed_df, column_name):
        # Get indices of non-null values in the column
        non_null_indices = processed_df[column_name].notnull()

        # Extract x and y values for interpolation
        x = np.where(non_null_indices)[0]  # Non-null indices as x values
        y = processed_df.loc[non_null_indices, column_name].values  # Non-null values as y values

        # Create an interpolation function (cubic spline interpolation)
        interpolator = interp1d(x, y, kind='cubic')

        # Generate indices for the entire range of the column
        full_indices = np.arange(len(processed_df))

        # Interpolate missing values
        interpolated_values = interpolator(full_indices)

        # Update the DataFrame with interpolated values
        processed_df[column_name] = np.where(
            processed_df[column_name].isnull(),
            interpolated_values[processed_df.index],
            processed_df[column_name]
        )

        return processed_df

    def process_data(self):
        processor = DataProcessor(self.username, self.password, self.host, self.database, self.table_name)
        processed_df = processor.fetch_data()

        col_val = ['Bearer Id', 'IMSI', 'Last Location Name', 'Last Location Name', 'IMEI',
                   'MSISDN/Number', 'Handset Manufacturer', 'Handset Type']
        for col in col_val:
            processed_df = processor.drop_null_rows(col)

        columns_to_drop = ['HTTP DL (Bytes)', 'HTTP UL (Bytes)']
        for col in columns_to_drop:
            processed_df = processor.drop_columns([col])

        cases = [
            # ... (existing code remains unchanged) ...
        ]

        for case in cases:
            related_cols = case['related_cols']
            target_cols = case['target_cols']
            processed_df = processor.assign_zero_based_on_condition(related_cols, target_cols)
            
        # Interpolate missing values in a specific column (example: 'Your_Column_Name')
        column_to_interpolate = 'Your_Column_Name'
        processed_df = self.interpolate_nonlinear(processed_df, column_to_interpolate)

        return processed_df
