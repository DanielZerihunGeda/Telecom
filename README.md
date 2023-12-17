# User Analytics in Telecommunication Industry

A comprehensive User Analytics project focused on analyzing user overview, engagement, experience, and satisfaction in the Telecommunication Industry. The project utilizes data samples provided in the `data` folder and implements various tools for analysis.

[![Build Status](https://github.com/DanielZerihunGeda/Telecom/workflows/Python%20CI/badge.svg)](https://github.com/DanielZerihunGeda/Telecom/actions)

## Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Creating a Virtual Environment](#virtual-env)
- [Usage](#usage)
 - [Data Loading](#data-loading)
  - [EDA](#EDA-Analysis)
- [Testing](#testing)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/DanielZerihunGeda/Telecom.git
 2. Navigate to the project directory:
    ```bash
    cd Telecom
    ```
 
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

be aware that the existing requirements.txt file includes all the packages for the project
   
If you prefer Conda as your package manager:

1. Open your terminal or command prompt.

2. Navigate to your project directory.

3. Run the following command to create a new Conda environment:

    ```bash
    conda create --name your_env_name python=3.12
    ```
    Replace `your_env_name` with the desired name for your environment e.g. week0 and `3.12` with your preferred Python version.

4. Activate the environment:

    ```bash
    conda activate your_env_name
    ```
If you prefer using `venv`, Python's built-in virtual environment module:

1. Open your terminal or command prompt.

2. Navigate to your project directory.

3. Run the following command to create a new virtual environment:

    ```bash
    python -m venv your_env_name
    ```

    Replace `your_env_name` with the desired name for your environment.

4. Activate the environment:

    - On Windows:

    ```bash
    .\your_env_name\scripts\activate
    ```

    - On macOS/Linux:

    ```bash
    source your_env_name/bin/activate
    ```

Now, your virtual environment is created and activated. You can install packages and run your Python scripts within this isolated environment. Don't forget to install required packages using `pip` or `conda` once the environment is activated.

## usage
## data-loading
In the src directory, there are two modules: Utility and DataCleaner.

1. Utility Module:

	Takes raw data hosted by PostgreSQL.

	Allows you to assign the following parameters is test.py in tests directory:
		Username
		Password
		Table name
		Database name

	Used for processing data before conducting Exploratory Data Analysis (EDA).

	The module passes the fetched data and contains necessary methods for cleaning up, including interpolation.

	Returns the processed data as a dataframe.

2. DataCleaner Module:

	Takes the data processed by the Utility module.

	Performs final cleaning steps.

	Returns the fully cleaned data for further EDA analysis.
## EDA-analysis

EDA Analysis Directory, you'll find essential functions for Exploratory Data Analysis (EDA). These functions cover various aspects:
Univariate Analysis:

Provides tools for analyzing individual variables.

Bivariate Analysis:

Allows the examination of relationships between two variables.

Multivariate Analysis:

Supports the analysis of interactions between multiple variables.

Outlier Analysis:

Identifies and handles outliers within the dataframe. for a given columns


