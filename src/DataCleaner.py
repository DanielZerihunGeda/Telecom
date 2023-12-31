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
""" columns to be interpolated based on appropriate mechanisms to ensure data integerity and conviniece analysis"""

        self.columns_to_interpolate =['Avg RTT DL (ms)', 'Avg RTT UL (ms)'
                                  ,'TCP DL Retrans. Vol (Bytes)',
                                 'TCP UL Retrans. Vol (Bytes)']
    
    def process_data(self):
        processor = DataProcessor(self.username, self.password, self.host, self.database, self.table_name)
        processed_df = processor.fetch_data()
""" 
    Dropping null values from the columns which are listed below, because the missing values from those columns

    indicates that the user xdr session is not recored accurately it might be the user on 'VPN' network for instance

    so the data measured for each attribute are not the actual data, or the other reason might be technical problem

"""
        col_val = ['Bearer Id', 'IMSI', 'Last Location Name', 'Last Location Name', 'IMEI',
                   'MSISDN/Number', 'Handset Manufacturer', 'Handset Type']
        for col in col_val:
            processed_df = processor.drop_null_rows(col)
"""
    we don't need ['HTTP DL (Bytes)', 'HTTP UL (Bytes)'] col to for our Expolraotry Data Analysis due to they are missing in
    
    large proportion compared to the data set we have
 
"""

        columns_to_drop = ['HTTP DL (Bytes)', 'HTTP UL (Bytes)']
        for col in columns_to_drop:
            processed_df = processor.drop_columns([col])
""" 
    those cols in cases variable are columns which are interelated with each other each columns 
    
    for a given interrelated columns they can not have non-zero value simultaneosly if one of 
    
    the attribute has non zero values we will assign 0 for the rest of the interrelated columns
"""
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
        col_interpolated = ['Avg RTT DL (ms)','Avg RTT UL (ms)']
        processed_df=  processor.interpolate_columns(col_interpolated,window_size=5)
        processed_df = processed_df
        for case in cases:
            related_cols = case['related_cols']
            target_cols = case['target_cols']
            processed_df = processor.assign_zero_based_on_condition(related_cols, target_cols)

        
        return processed_df  # Return the processed data
    

