# Reading Data and DataFrame Basics

This lesson introduces Pandas DataFrames by reading an Excel file and inspecting its structure.

## Prerequisites

Install Pandas and an Excel engine such as `openpyxl`:

```bash
pip install pandas openpyxl
```

## Topics Covered

- Importing Pandas
- Checking the Pandas version
- Reading an Excel file with `pd.read_excel()`
- Selecting categorical and numeric columns
- Checking a DataFrame's type, length, columns, and shape
- Finding missing values
- Viewing the first and last rows
- Inspecting DataFrame details with `info()`

## Basic Example

```python
import pandas as pd

# Update this path if the dataset is stored elsewhere.
df = pd.read_excel(
    r'C:\Users\Nikhil\NVS Code\Pandas\01_first_code\data.xlsx'
)

# Select columns by category
df_cat = df[['CountryName', 'CountryCode', 'IncomeGroup']]
df_num = df[['BirthRate', 'InternetUsers']]

# Inspect the DataFrame
type(df)
len(df)
df.columns
df.shape

# Check missing values
df.isnull()
df.isnull().sum()

# Preview and summarize the data
df.head()
df.tail()
df.info()
```

## Important DataFrame Attributes and Methods

| Expression | Purpose |
|---|---|
| `df.shape` | Returns the number of rows and columns |
| `df.columns` | Lists the column labels |
| `df.head()` | Displays the first five rows |
| `df.tail()` | Displays the last five rows |
| `df.info()` | Shows column types, non-null counts, and memory usage |
| `df.isnull().sum()` | Counts missing values in each column |

## Notebook

Open [`ReadingData-DataFrame.ipynb`](ReadingData-DataFrame.ipynb) to follow the lesson interactively.
