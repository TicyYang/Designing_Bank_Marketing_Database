# ETL_with_PySpark

This project utilizes the Bank Marketing dataset from UC Irvine, sourced from [UCI Machine Learning Repository - Bank Marketing](https://archive.ics.uci.edu/dataset/222/bank+marketing).

## Project Overview

Applying the ETL (Extract, Transform, Load) method to clean and preprocess the raw data and store it in a PostgreSQL database. Designing appropriate table structures based on different attributes and data types, dividing the data into three distinct tables: client, campaign, and economics.

- **create_database.sql**:  Create the database.
- **create_tables.sql**:  Create client, campaign, economics tables.
- **data_cleaning.ipynb**:  Data cleaning with PySpark.
- **database_import.ipynb**:  Import the cleaned data into the database.

## ER Diagram

![Entity Relationship Diagram](er_diagram.png)

## License

"Bank Marketing" dataset (c) by S. Moro, P. Rita, P. Cortez - UCI Machine Learning Repository.
