from scipy.interpolate import interp1d
from utility import DataProcessor
import pandas as pd
from datetime import datetime

class ProcessData:
    def __init__(self, username, password, host, database, table_name):
        self.username = username
        self.password = password
        self.host = host
        self.database = database
        self.table_name = table_name
        self.columns_to_interpolate =['Avg RTT DL (ms)', 'Avg RTT UL (ms)',
                                  ,'TCP DL Retrans. Vol (Bytes)',
                                 'TCP UL Retrans. Vol (Bytes)']
    
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
            {
                'related_cols': ['Nb of sec with 125000B < Vol DL', 'Nb of sec with 31250B < Vol DL < 125000B',
                                 'Nb of sec with 6250B < Vol DL < 31250B', 'Nb of sec with Vol DL < 6250B'],
                'target_cols': ['Nb of sec with 125000B < Vol DL', 'Nb of sec with 31250B < Vol DL < 125000B',
                                'Nb of sec with 6250B < Vol DL < 31250B', 'Nb of sec with Vol DL < 6250B']
            },
            {
                'related_cols': ['Nb of sec with 1250B < Vol UL < 6250B', 'Nb of sec with 37500B < Vol UL',
                                 'Nb of sec with 6250B < Vol UL < 37500B', 'Nb of sec with Vol UL < 1250B'],
                'target_cols': ['Nb of sec with 1250B < Vol UL < 6250B', 'Nb of sec with 37500B < Vol UL',
                                'Nb of sec with 6250B < Vol UL < 37500B', 'Nb of sec with Vol UL < 1250B']
            },
            {
                'related_cols': ['DL TP < 50 Kbps (%)', '50 Kbps < DL TP < 250 Kbps (%)', '250 Kbps < DL TP < 1 Mbps (%)',
                                 'DL TP > 1 Mbps (%)'],
                'target_cols': ['DL TP < 50 Kbps (%)', '50 Kbps < DL TP < 250 Kbps (%)', '250 Kbps < DL TP < 1 Mbps (%)',
                                'DL TP > 1 Mbps (%)']
            },
            {
                'related_cols': ['UL TP < 10 Kbps (%)', '10 Kbps < UL TP < 50 Kbps (%)', '50 Kbps < UL TP < 300 Kbps (%)',
                                 'UL TP > 300 Kbps (%)'],
                'target_cols': ['UL TP < 10 Kbps (%)', '10 Kbps < UL TP < 50 Kbps (%)', '50 Kbps < UL TP < 300 Kbps (%)',
                                'UL TP > 300 Kbps (%)']
            },
        ]

        for case in cases:
            related_cols = case['related_cols']
            target_cols = case['target_cols']
            processed_df = processor.assign_zero_based_on_condition(related_cols, target_cols)
            
        return processed_df  # Return the processed data

