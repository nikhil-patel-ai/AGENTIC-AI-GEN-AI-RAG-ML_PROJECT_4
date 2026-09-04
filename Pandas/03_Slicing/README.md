# Pandas Slicing and Data Analysis

This lesson uses a country statistics dataset to practice slicing, selecting, transforming, filtering, and visualizing Pandas DataFrames.

## Prerequisites

Install the required packages:

```bash
pip install pandas openpyxl matplotlib seaborn
```

## Topics Covered

- Reading an Excel file into a DataFrame
- Inspecting DataFrame dimensions and contents
- Slicing rows with Python slice notation
- Selecting one or multiple columns
- Describing numeric and categorical data
- Creating and dropping columns
- Renaming columns
- Filtering rows with conditions
- Finding unique and distinct values
- Visualizing distributions and relationships with Seaborn

## Load the Dataset

```python
import pandas as pd

df = pd.read_excel(
    r'C:\Users\Nikhil\NVS Code\Pandas\01_first_code\data.xlsx'
)
```

## Row Slicing

Pandas DataFrames support Python-style row slicing:

```python
df[:]              # All rows
df[10:21]         # Rows 10 through 20
df[10:150:20]     # Rows 10 through 149, stepping by 20
df[::10]          # Every tenth row
df[::-1]          # Rows in reverse order
df[::-50]         # Reverse order with a step of 50
```

## Column Selection

```python
# Select one column as a Series
country_names = df['CountryName']

# Select several columns as a DataFrame
df_cat = df[['CountryName', 'CountryCode', 'IncomeGroup']]
df_num = df[['BirthRate', 'InternetUsers']]
```

## Inspect and Summarize Data

```python
df.shape             # Number of rows and columns
df.columns           # Column names
df.head(3)           # First three rows
df.tail()            # Last five rows
df.info()            # Data types and non-null counts
df.isnull().sum()    # Missing values by column
df.describe()        # Numeric summary statistics
df_cat.describe()    # Summary of categorical columns
```

## Create, Drop, and Rename Columns

```python
# Create a calculated column
df['newCalc'] = df['BirthRate'] * df['InternetUsers']

# Remove the calculated column
df = df.drop('newCalc', axis=1)

# Rename all columns by assigning a new list
df.columns = ['a', 'b', 'c', 'd', 'e']

# Restore the original names
df.columns = [
    'CountryName', 'CountryCode', 'BirthRate',
    'InternetUsers', 'IncomeGroup'
]
```

## Filter Rows

Boolean expressions can be used to select matching rows:

```python
# Internet usage below 3 percent
df[df['InternetUsers'] < 3]

# Birth rate above 40
df[df['BirthRate'] > 40]

# Combine conditions with &, placing each condition in parentheses
df[(df['BirthRate'] > 40) & (df['InternetUsers'] < 2)]
```

## Unique Values

```python
df['IncomeGroup'].unique()   # Return distinct income groups
df['IncomeGroup'].nunique()  # Count distinct income groups
```

## Visualize the Data

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = (6, 2)

# Distribution of internet usage
sns.displot(df['InternetUsers'], bins=10)

# Birth rate by income group
sns.boxplot(data=df, x='IncomeGroup', y='BirthRate')

# Relationship between internet usage and birth rate
sns.lmplot(data=df, x='InternetUsers', y='BirthRate', fit_reg=True)

# Color the relationship by income group
sns.lmplot(
    data=df,
    x='InternetUsers',
    y='BirthRate',
    fit_reg=True,
    hue='IncomeGroup'
)
```

## Notebook

Open [`Slicing.ipynb`](Slicing.ipynb) to run the examples interactively.
