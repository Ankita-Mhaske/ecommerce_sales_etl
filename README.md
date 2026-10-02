# E-commerce Sales ETL Pipeline

A small data engineering project built using Python and Pandas. The project takes raw e-commerce sales data from a CSV file, cleans and transforms it, and then stores the cleaned data in a SQLite database for analysis.

The main goal of this project is to understand how a basic ETL pipeline works using a real-looking sales dataset.


## What this project demonstrates

* Python
* Pandas
* CSV data processing
* Data cleaning and validation
* Data transformation
* ETL pipeline concepts
* SQLite
* SQL for basic analysis


## Project flow


raw_sales.csv
     |
     v
Read data using Pandas
     |
     v
Clean and check the data
     |
     |-- remove duplicate orders
     |-- check quantity and price
     |-- handle missing state
     |-- fix incorrect sales amount
     |-- add order month
     |
     v
clean_sales.csv
     |
     v
Save data in SQLite
     |
     v
Run SQL queries for analysis


## Folder structure


ecommerce_sales_etl/
│
├── data/
│   └── raw_sales.csv
│
├── src/
│   └── etl_pipeline.py
│
├── sql/
│   └── analysis_queries.sql
│
├── requirements.txt
└── README.md


After running the pipeline, these files are also created inside the `data` folder:


clean_sales.csv
sales.db



## How to run

### 1. Clone the repository

git clone <your-github-repository-url>
cd ecommerce_sales_etl


### 2. Install the required package


pip install -r requirements.txt


### 3. Run the ETL pipeline


python src/etl_pipeline.py


The script will create:

* data/clean_sales.csv
* data/sales.db

The terminal also shows how many rows were processed and how many duplicate or invalid records were found.

### 4. Run SQL queries

The SQL queries are available in:


sql/analysis_queries.sql


They can be run on the `sales` table in `data/sales.db`.

## Example business questions

The sales data can be used to answer questions such as:

* What is the total sales amount?
* Which products have the highest sales?
* Which category has the highest sales?
* How do sales change month by month?
* Which states have the highest sales?
* What is the average order value?

## Resume description

**E-commerce Sales ETL Pipeline | Python, Pandas, SQL, SQLite**

* Built a simple ETL pipeline to read e-commerce sales data from a CSV file and process it using Python and Pandas.
* Cleaned and validated the data by removing duplicate orders, checking quantity and price values, handling missing states, and correcting sales amounts.
* Stored the cleaned data in SQLite and prepared SQL queries for basic sales analysis.


## Output

After running the pipeline, the cleaned data is saved as:


data/clean_sales.csv


The cleaned data is also stored in:

data/sales.db


The SQLite database contains a table named `sales`.
