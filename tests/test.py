from DataCleaner import ProcessData  # Assuming DataCleaner is your module name

def main():
    # Fill in your database credentials based on how your sql server is hosted (Postgresql)
    username = 'your_username'
    password = 'your_password'
    host = 'your_host'
    database = 'your_database'
    table_name = 'your_table_name'

    # Create an instance of ProcessData
    data_processor = ProcessData(username, password, host, database, table_name)

    # Process the data
    processed_data = data_processor.process_data()

    # Display or save the processed data as needed
    print(processed_data.head())  # Display the first few rows of the processed data

if __name__ == "__main__":
    main()

