# Pandas Functions and Data Exploration

This lesson uses a country statistics dataset to practice common Pandas DataFrame operations and basic visualization.

## Prerequisites

Install the required packages:

```bash
pip install pandas openpyxl matplotlib seaborn
```

The notebook expects the Excel dataset at `../01_first_code/data.xlsx`.

## Topics Covered

- Importing Pandas and checking its version
- Inspecting DataFrame types, dimensions, columns, and missing values
- Viewing the first and last rows
- Slicing rows with Python slice notation
- Selecting categorical and numeric columns
- Creating and removing calculated columns
- Renaming DataFrame columns
- Filtering rows with boolean conditions
- Finding unique values and counting distinct values
- Creating distribution, box, and regression plots with Seaborn

## Load the Dataset

```python
import pandas as pd

# Update the path if the dataset is stored elsewhere.
df = pd.read_excel(r'../01_first_code/data.xlsx')
```

## Inspect the DataFrame

```python
type(df)
len(df)
df.columns
df.shape
df.isnull().sum()
df.head()
df.tail()
df.info()
```

## Slice Rows and Select Columns

```python
# Row slicing
df[:]
df[10:21]
df[::10]
df[::-1]

# Column selection
country_data = df[['CountryName', 'CountryCode', 'IncomeGroup']]
numeric_data = df[['BirthRate', 'InternetUsers']]
```

## Create, Remove, and Rename Columns

```python
# Create a calculated column
df['newCalc'] = df['BirthRate'] * df['InternetUsers']

# Remove the calculated column
df = df.drop('newCalc', axis=1)

# Rename columns by assigning a new list
df.columns = [
    'CountryName', 'CountryCode', 'BirthRate',
    'InternetUsers', 'IncomeGroup'
]
```

## Filter Rows

```python
# Countries with less than 3 percent Internet usage
df[df['InternetUsers'] < 3]

# Countries with a birth rate above 40
df[df['BirthRate'] > 40]

# Combine multiple conditions
df[(df['BirthRate'] > 40) & (df['InternetUsers'] < 2)]
```

## Descriptive Statistics and Unique Values

```python
df.describe()
df[['CountryName', 'CountryCode', 'IncomeGroup']].describe()
df['IncomeGroup'].unique()
df['IncomeGroup'].nunique()
```

## Visualize the Data

```python
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['figure.figsize'] = (6, 2)

sns.displot(df['InternetUsers'], bins=10)
sns.boxplot(data=df, x='IncomeGroup', y='BirthRate')
sns.lmplot(
    data=df,
    x='InternetUsers',
    y='BirthRate',
    hue='IncomeGroup',
    fit_reg=True,
)
```

## Notebook

Open [`pandas.ipynb`](pandas.ipynb) to work through the examples interactively.
