# Introduction to Pandas - First Code

This notebook is a beginner-friendly introduction to Pandas, one of the most powerful data manipulation libraries in Python. It covers loading data, exploring datasets, filtering, and basic visualization.

---

## Table of Contents

1. [What is Pandas?](#what-is-pandas)
2. [Installation & Import](#installation--import)
3. [Reading Data](#reading-data)
4. [DataFrame Basics](#dataframe-basics)
5. [Exploring Data](#exploring-data)
6. [Slicing](#slicing)
7. [Column Selection](#column-selection)
8. [Descriptive Statistics](#descriptive-statistics)
9. [Creating and Dropping Columns](#creating-and-dropping-columns)
10. [Renaming Columns](#renaming-columns)
11. [Filtering Data](#filtering-data)
12. [Unique Values](#unique-values)
13. [Data Visualization](#data-visualization)

---

## What is Pandas?

Pandas is a Python library that provides:
- **DataFrames**: 2D tables with rows and columns (like Excel or SQL tables)
- **Series**: 1D arrays with labeled indices
- **Data manipulation**: Cleaning, transforming, and analyzing data
- **Easy I/O**: Reading/writing CSV, Excel, SQL, JSON, etc.

**Why Pandas?**
- Intuitive syntax for data operations
- Handles missing data
- Powerful filtering and grouping
- Integration with visualization libraries
- Industry standard for data science

---

## Installation & Import

### Installation

```bash
# Using pip
pip install pandas

# Using conda
conda install pandas
```

### Import

```python
import pandas as pd

# Check version
pd.__version__
# Output: '1.3.5' (or your installed version)
```

---

## Reading Data

Pandas supports reading data from multiple formats:

### From Excel Files
```python
df = pd.read_excel(r'C:\Users\Nikhil\NVS Code\Pandas\01_first_code\data.xlsx')
```

### From CSV Files
```python
df = pd.read_csv('data.csv')
```

### From Other Formats
```python
# JSON
df = pd.read_json('data.json')

# SQL Database
df = pd.read_sql('SELECT * FROM table', connection)

# HTML
df = pd.read_html('https://example.com')

# Clipboard
df = pd.read_clipboard()
```

---

## DataFrame Basics

### Understanding DataFrames

A **DataFrame** is a 2D table structure with:
- **Rows**: Individual records/observations
- **Columns**: Features/variables
- **Index**: Row labels (0, 1, 2, ... by default)

### Basic Properties

```python
# Type of object
type(df)
# Output: <class 'pandas.core.frame.DataFrame'>

# Number of rows
len(df)
# Output: 245

# Column names
df.columns
# Output: Index(['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup'], dtype='object')

# Number of columns
len(df.columns)
# Output: 5

# Shape (rows, columns)
df.shape
# Output: (245, 5)
```

### Null Value Check

```python
# Check for null values
df.isnull()
# Returns boolean DataFrame showing True where null exists

# Count null values per column
df.isnull().sum()
# Output:
# CountryName      0
# CountryCode      0
# BirthRate        4
# InternetUsers    2
# IncomeGroup      0
```

---

## Exploring Data

### head() - First Rows

```python
# First 5 rows (default)
df.head()

# First 3 rows
df.head(3)
# Output:
#         CountryName CountryCode  BirthRate  InternetUsers      IncomeGroup
# 0      Afghanistan           AF       46.6           7.76          Low income
# 1          Albania           AL       18.2          44.90  Upper middle income
# 2          Algeria           DZ       24.3          14.00  Lower middle income
```

### tail() - Last Rows

```python
# Last 5 rows (default)
df.tail()

# Last 3 rows
df.tail(3)
```

### info() - Dataset Information

```python
df.info()
# Output:
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 245 entries, 0 to 244
# Data columns (total 5 columns):
#  #   Column         Non-Null Count  Dtype
# ---  ------         --------------  -----
#  0   CountryName    245 non-null    object
#  1   CountryCode    245 non-null    object
#  2   BirthRate      241 non-null    float64
#  3   InternetUsers  243 non-null    float64
#  4   IncomeGroup    245 non-null    object
```

**What it shows:**
- Number of rows
- Column names and data types
- Non-null count (missing data info)
- Memory usage

---

## Slicing

Slicing retrieves specific rows based on position.

### Basic Slicing

```python
# All rows
df[:]

# Rows 10 to 20 (inclusive of 10, exclusive of 21)
df[10:21]
# Output: 11 rows (rows 10-20)

# Rows 10 to 150 with step 20
df[10:150:20]
# Output: rows 10, 30, 50, 70, 90, 110, 130, 150

# Every 10th row from start
df[::10]
# Output: rows 0, 10, 20, 30, 40, ...

# Reverse order (last to first)
df[::-1]
# Output: DataFrame in reverse order

# Every 50th row in reverse
df[::-50]
```

### Slicing Syntax

```
df[start:stop:step]

start: Beginning index (default: 0)
stop:  Ending index (exclusive)
step:  Interval between rows (default: 1)
```

---

## Column Selection

### Single Column

```python
# Accessing a single column
df['CountryName']
# Returns a Series (1D array)

# Type
type(df['CountryName'])
# Output: <class 'pandas.core.series.Series'>

# Alternative syntax
df.CountryName  # Works only if column name is valid Python identifier
```

### Multiple Columns

```python
# Select multiple columns (returns DataFrame)
df[['CountryName', 'CountryCode']]

# Three columns
df[['CountryName', 'CountryCode', 'IncomeGroup']]

# Create subset with categorical variables
df_cat = df[['CountryName', 'CountryCode', 'IncomeGroup']]
# Shape: (245, 3)

# Create subset with numerical variables
df_num = df[['BirthRate', 'InternetUsers']]
# Shape: (245, 2)
```

**Key Point:** Use double brackets `[[]]` for multiple columns, single brackets `[]` for single column.

---

## Descriptive Statistics

### describe() Function

Provides summary statistics for numerical columns:

```python
# Statistics for numerical columns
df.describe()
# Output:
#        BirthRate  InternetUsers
# count    241.000         243.000
# mean      20.186          36.814
# std       12.265          29.756
# min        7.700           0.260
# 25%        11.450          10.140
# 50%        17.600          33.210
# 75%        28.900          61.480
# max       50.700          95.170

# Statistics for categorical columns
df_cat.describe()
# Output:
#        CountryName CountryCode IncomeGroup
# count          245         245         245
# unique         245         245           4
# top      Afghanistan          AF   Low income
# freq             1           1          49
```

### What it Returns

**For numerical columns:**
- **count**: Non-null values
- **mean**: Average
- **std**: Standard deviation
- **min**: Minimum value
- **25%, 50%, 75%**: Quartiles (percentiles)
- **max**: Maximum value

**For categorical columns:**
- **count**: Non-null values
- **unique**: Number of distinct values
- **top**: Most frequent value
- **freq**: Frequency of top value

---

## Creating and Dropping Columns

### Creating New Columns

```python
# Calculate new column
result = df.BirthRate * df.InternetUsers
# This returns a Series

# Add as new column to DataFrame
df['newCalc'] = df.BirthRate * df.InternetUsers

# Verify
df['newCalc']
# All rows now have calculated values

# Check columns
df.columns
# Output: Index(['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup', 'newCalc'], ...)
```

### Dropping Columns

```python
# Remove column
df = df.drop('newCalc', axis=1)

# Verify removal
df.columns
# 'newCalc' is gone

# Drop multiple columns
df = df.drop(['col1', 'col2'], axis=1)

# axis Parameter:
# axis=0: Drop rows
# axis=1: Drop columns
```

---

## Renaming Columns

### Method 1: Replace All Column Names

```python
# Rename all columns at once
df.columns = ['a', 'b', 'c', 'd', 'e']
df.head(1)
# All columns are renamed

# Rename back to original names
df.columns = ['CountryName', 'CountryCode', 'BirthRate', 'InternetUsers', 'IncomeGroup']
```

### Method 2: Rename Specific Columns

```python
# Rename specific columns using dictionary
df = df.rename(columns={'OldName': 'NewName', 'AnotherOld': 'AnotherNew'})

# Example
df = df.rename(columns={'CountryName': 'Country', 'BirthRate': 'BR'})
```

---

## Filtering Data

Filtering uses **boolean indexing** to select rows meeting specific conditions.

### Single Condition

```python
# Boolean comparison
df['InternetUsers'] < 3
# Returns Series of True/False for each row

# Filter rows
df[df['InternetUsers'] < 3]
# Returns DataFrame with only rows where InternetUsers < 3

# Count matching rows
len(df[df['InternetUsers'] < 3])
# Output: 47 countries

# Example with another column
df[df['BirthRate'] > 40]
# Returns countries with high birth rates
len(df[df['BirthRate'] > 40])
# Output: 58 countries
```

### Multiple Conditions

Use `&` (AND) and `|` (OR) operators:

```python
# AND condition (both must be true)
df[(df.BirthRate > 40) & (df.InternetUsers < 2)]
# Countries with high birth rate AND low internet users

# Count
len(df[(df.BirthRate > 40) & (df.InternetUsers < 2)])
# Output: 11 countries

# OR condition (either can be true)
df[(df.BirthRate > 40) | (df.InternetUsers > 80)]

# NOT condition (negate)
df[~(df.BirthRate > 40)]  # NOT greater than 40
```

**Important:** Use `&` (AND), `|` (OR), `~` (NOT). Do NOT use `and`, `or`, `not`.

### Comparison Operators

| Operator | Meaning |
|----------|---------|
| `<` | Less than |
| `>` | Greater than |
| `<=` | Less than or equal |
| `>=` | Greater than or equal |
| `==` | Equal to |
| `!=` | Not equal to |
| `isin()` | In a list of values |

### Advanced Filtering

```python
# Check if value in list
df[df['IncomeGroup'].isin(['Low income', 'Lower middle income'])]

# String operations
df[df['CountryName'].str.startswith('A')]  # Countries starting with A

# Between values
df[df['BirthRate'].between(20, 30)]
```

---

## Unique Values

### unique() - Get Unique Values

```python
# Get all unique income groups
df.IncomeGroup.unique()
# Output: array(['Low income', 'Upper middle income', 'Lower middle income', 'High income'], dtype=object)

# Returns array of unique values in order they appear
```

### nunique() - Count Unique Values

```python
# Count distinct income groups
df.IncomeGroup.nunique()
# Output: 4

# Useful for understanding categorical variables
df['IncomeGroup'].value_counts()
# Output:
# Low income              49
# Lower middle income     47
# High income             44
# Upper middle income     44
```

---

## Data Visualization

### Setup

```python
import matplotlib.pyplot as plt
import seaborn as sns

# Display plots inline in Jupyter
%matplotlib inline

# Set figure size
plt.rcParams['figure.figsize'] = (6, 4)

# Suppress warnings
import warnings
warnings.filterwarnings('ignore')
```

### Distribution Plot (distplot)

Shows distribution of a numerical variable.

```python
# Distribution plot
sns.distplot(df['InternetUsers'])
# Shows histogram with KDE (kernel density estimate)

# Note: distplot is deprecated, use displot instead
sns.displot(df['InternetUsers'])  # Modern alternative
```

### Histogram (displot)

```python
# Histogram with custom bins
sns.displot(df['InternetUsers'], bins=10)
# Divides data into 10 bins and shows frequency

# Higher bins = more detail
sns.displot(df['InternetUsers'], bins=20)
```

**Use When:** You want to see the distribution of a continuous variable.

### Box Plot (boxplot)

Shows distribution of numerical variable by categories.

```python
sns.boxplot(data=df, x="IncomeGroup", y="BirthRate")
# Compares BirthRate across different IncomeGroups

# Shows: min, Q1 (25%), median, Q3 (75%), max, outliers
```

**Use When:** You want to compare distributions across categories.

### Scatter Plot with Regression (lmplot)

Shows relationship between two variables.

```python
# Scatter plot with regression line
sns.lmplot(data=df, x="InternetUsers", y="BirthRate")
# Shows trend line (linear model)

# Without regression line
sns.lmplot(data=df, x="InternetUsers", y="BirthRate", fit_reg=False)

# With regression line
sns.lmplot(data=df, x="InternetUsers", y="BirthRate", fit_reg=True)

# Color by category (hue)
sns.lmplot(data=df, x="InternetUsers", y="BirthRate", fit_reg=False, hue="IncomeGroup")
# Each income group has different color

# With regression per group
sns.lmplot(data=df, x="InternetUsers", y="BirthRate", fit_reg=True, hue="IncomeGroup")
# Separate trend lines for each income group
```

**Use When:** You want to see correlation between two variables.

---

## Complete Workflow Example

```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Load data
df = pd.read_excel('data.xlsx')

# 2. Explore
print(df.shape)         # Check size
print(df.info())        # Check columns and types
print(df.head())        # View first rows

# 3. Check quality
print(df.isnull().sum())  # Check missing values

# 4. Filter
high_birthrate = df[df['BirthRate'] > 40]
print(f"Countries with high birth rate: {len(high_birthrate)}")

# 5. Create column
df['BR_per_User'] = df['BirthRate'] / df['InternetUsers']

# 6. Analyze
print(df.describe())

# 7. Visualize
sns.lmplot(data=df, x="InternetUsers", y="BirthRate", hue="IncomeGroup")
plt.show()
```

---

## Common Operations Reference

| Task | Code |
|------|------|
| Read data | `pd.read_excel('file.xlsx')` |
| Check shape | `df.shape` |
| View first rows | `df.head()` |
| View last rows | `df.tail()` |
| Check columns | `df.columns` |
| Check null values | `df.isnull().sum()` |
| Get statistics | `df.describe()` |
| Select column | `df['ColName']` |
| Select columns | `df[['Col1', 'Col2']]` |
| Filter rows | `df[df['Col'] > value]` |
| Add column | `df['NewCol'] = calculation` |
| Drop column | `df.drop('ColName', axis=1)` |
| Rename columns | `df.rename(columns={...})` |
| Unique values | `df['Col'].unique()` |
| Count unique | `df['Col'].nunique()` |

---

## Tips & Best Practices

1. **Always explore first**: Use `head()`, `info()`, `describe()` to understand data
2. **Check for missing values**: `isnull().sum()` to identify problems
3. **Use meaningful variable names**: Makes code more readable
4. **Filter step-by-step**: Start with one condition, add more as needed
5. **Create subsets**: Extract relevant columns to focus analysis
6. **Document your steps**: Add comments explaining transformations
7. **Validate results**: Verify filtered counts and calculations

---

## Common Errors & Solutions

### Error: KeyError - Column not found
```python
# Wrong
df['CountryName']  # If column name has typo

# Solution
print(df.columns)  # Check exact column names
df['CountryName']  # Use correct name
```

### Error: TypeError - Can't use 'and', 'or' in boolean indexing
```python
# Wrong
df[df['Col1'] > 5 and df['Col2'] < 10]

# Correct
df[(df['Col1'] > 5) & (df['Col2'] < 10)]
```

### Error: Forgot to assign result
```python
# Wrong
df.drop('Col', axis=1)  # Does nothing to df

# Correct
df = df.drop('Col', axis=1)  # Assigns result back
```

---

## Learning Path

1. **Start Here:** Load data, explore structure, check quality
2. **Then:** Filter data, select columns, create new columns
3. **Next:** Descriptive statistics, understand distributions
4. **Finally:** Visualization, identify patterns, draw conclusions

---

## Practice Exercises

1. Load a dataset and check its shape and columns
2. Filter rows where a numerical column exceeds a threshold
3. Combine multiple filter conditions using & and |
4. Create a new column based on existing columns
5. Find and display unique values in a categorical column
6. Create distribution plots for numerical variables
7. Compare two variables using scatter plot with hue
8. Calculate and display descriptive statistics
9. Find countries/rows with missing values
10. Rename columns and drop unnecessary columns

---

## Next Steps

Learn more about:
- **GroupBy operations**: Aggregate data by groups
- **Merging DataFrames**: Combine multiple datasets
- **Pivoting**: Reshape data
- **Time series**: Working with dates
- **Advanced visualization**: Heatmaps, pair plots
- **Data cleaning**: Handling missing values, duplicates
- **Export data**: Save to CSV, Excel, SQL

---

## References

- [Official Pandas Documentation](https://pandas.pydata.org/docs/)
- [Pandas Cheat Sheet](https://pandas.pydata.org/Pandas_Cheat_Sheet.pdf)
- [Seaborn Visualization](https://seaborn.pydata.org/)
- [Matplotlib Documentation](https://matplotlib.org/)

---

## Summary

This notebook covered:
- Loading data with `read_excel()`
- Exploring with `shape`, `columns`, `head()`, `tail()`, `info()`
- Slicing rows with positional indexing
- Selecting columns (single and multiple)
- Filtering with boolean indexing
- Creating and dropping columns
- Computing statistics with `describe()`
- Finding unique values
- Visualizing with seaborn and matplotlib

These fundamentals form the foundation for data analysis with Pandas!
