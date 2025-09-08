# 📊 Data Analytics Cheat Sheet - Python, Pandas & NumPy

## 🐍 Python Basics

### Import Libraries
```python
import pandas as pd          # Data manipulation
import numpy as np           # Numerical operations
```

### Working with Variables
```python
# Creating variables
my_list = [1, 2, 3, 4]      # List
my_dict = {'a': 1, 'b': 2}  # Dictionary

# Type checking
type(variable)               # Check variable type
isinstance(x, int)           # Check if x is integer
```

### List Comprehensions
```python
# Basic list comprehension
[x*2 for x in my_list]       # Double each element

# With condition
[x for x in my_list if x > 2]  # Filter elements > 2

# Nested comprehension
[x*y for x in [1,2] for y in [3,4]]  # All combinations
```

---

## 🐼 Pandas Essentials

### Loading Data
```python
# Read CSV file
df = pd.read_csv('filename.csv')

# Read with specific encoding
df = pd.read_csv('file.csv', encoding='utf-8')

# Read only specific columns
df = pd.read_csv('file.csv', usecols=['col1', 'col2'])
```

### The "Big 3" - Essential Data Exploration
```python
df.head()        # First 5 rows - see data structure
df.head(10)      # First 10 rows

df.info()        # Data types, non-null counts, memory usage

df.describe()    # Statistical summary of numerical columns
```

### Basic DataFrame Operations
```python
# Shape and size
df.shape         # (rows, columns)
len(df)          # Number of rows
df.columns       # Column names
df.dtypes        # Data types of each column

# Basic statistics
df.mean()        # Mean of all numeric columns
df['col'].mean() # Mean of specific column
df.sum()         # Sum
df.count()       # Count non-null values
```

### Data Selection - loc vs iloc
```python
# iloc - INTEGER POSITION based indexing
df.iloc[0]           # First row
df.iloc[0:5]         # First 5 rows
df.iloc[0:5, 0:3]    # First 5 rows, first 3 columns
df.iloc[:, 2]        # All rows, third column

# loc - LABEL based indexing
df.loc[0]            # Row with index 0
df.loc[0:5]          # Rows 0 to 5 (inclusive!)
df.loc[:, 'column']  # All rows, specific column
df.loc[df['col'] > 5]  # Rows where condition is true
df.loc[0:5, ['col1', 'col2']]  # Specific rows and columns
```

### Column Operations
```python
# Accessing columns
df['column_name']           # Returns Series
df[['col1', 'col2']]       # Returns DataFrame

# Adding new columns
df['new_col'] = df['col1'] + df['col2']
df['category'] = 'value'    # Constant value

# Renaming columns
df.rename(columns={'old': 'new'})
df.columns = ['new1', 'new2', ...]  # Rename all
```

### Data Cleaning & Type Conversion
```python
# Check for null values
df.isnull()              # Boolean mask of nulls
df.isnull().sum()        # Count nulls per column
df.isnull().sum().sum()  # Total nulls in DataFrame

# Handle missing values
df.dropna()              # Drop rows with any null
df.dropna(axis=1)        # Drop columns with any null
df.fillna(0)             # Fill nulls with 0
df.fillna(df.mean())     # Fill with mean
df['col'].fillna(df['col'].median())  # Fill with median

# Check current data types
df.dtypes                # All column types
df['col'].dtype          # Single column type
df.info()               # Complete type information

# Data type conversion - Basic
df['col'] = df['col'].astype(int)      # Convert to integer
df['col'] = df['col'].astype(float)    # Convert to float
df['col'] = df['col'].astype(str)      # Convert to string

# Safe numeric conversion (handles errors)
df['col'] = pd.to_numeric(df['col'], errors='coerce')  # Converts bad values to NaN
df['col'] = pd.to_numeric(df['col'], errors='ignore')  # Keeps original if can't convert

# Convert multiple columns at once
numeric_columns = ['col1', 'col2', 'col3']
for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Convert object columns to numeric (common with CSV imports)
# Example: 'ESTRATO 1' -> 1
df['estrato'] = df['estrato'].str.extract('(\d+)').astype(int)

# Convert all object columns that should be numeric
def convert_to_numeric(df):
    for col in df.columns:
        if df[col].dtype == 'object':
            try:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            except:
                pass  # Keep as object if conversion fails
    return df

# Change multiple column types at once
df = df.astype({
    'col1': 'int32',
    'col2': 'float64',
    'col3': 'category',
    'col4': 'bool'
})

# Datetime conversion
df['date'] = pd.to_datetime(df['date'])                   # Auto-detect format
df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')  # Specific format
df['date'] = pd.to_datetime(df['date'], errors='coerce')  # Handle errors

# Category type (for memory efficiency)
df['category_col'] = df['category_col'].astype('category')
```

### Filtering Data
```python
# Single condition
df[df['column'] > 5]
df[df['column'] == 'value']
df[df['column'].isin(['val1', 'val2'])]

# Multiple conditions (use & and |, not 'and' or 'or')
df[(df['col1'] > 5) & (df['col2'] < 10)]
df[(df['col1'] == 'A') | (df['col2'] == 'B')]

# String operations
df[df['col'].str.contains('text')]
df[df['col'].str.startswith('prefix')]
```

### Sorting
```python
df.sort_values('column')                # Ascending
df.sort_values('column', ascending=False)  # Descending
df.sort_values(['col1', 'col2'])       # Multiple columns
df.nlargest(5, 'column')               # Top 5 by column
df.nsmallest(5, 'column')              # Bottom 5 by column
```

### GroupBy Operations
```python
# Basic groupby
df.groupby('column').mean()
df.groupby('column').size()     # Count per group
df.groupby('column')['target'].mean()  # Specific column

# Multiple aggregations
df.groupby('col').agg({
    'col1': 'mean',
    'col2': 'sum',
    'col3': 'count'
})

# Multiple groupby columns
df.groupby(['col1', 'col2']).mean()

# Common aggregations
.sum()      # Sum values
.mean()     # Average
.median()   # Median
.count()    # Count non-null
.size()     # Count all (including null)
.std()      # Standard deviation
.min()      # Minimum
.max()      # Maximum
.first()    # First value
.last()     # Last value
```

### Value Counts & Unique
```python
df['column'].value_counts()      # Frequency of each value
df['column'].value_counts(normalize=True)  # As percentages
df['column'].unique()            # Unique values
df['column'].nunique()           # Number of unique values
```

### Apply Functions
```python
# Apply to Series
df['col'].apply(lambda x: x*2)
df['col'].apply(function_name)

# Apply to DataFrame
df.apply(lambda x: x.max() - x.min())  # Column-wise
df.apply(lambda x: x.sum(), axis=1)    # Row-wise
```

---

## 🔢 NumPy Essentials

### Creating Arrays
```python
# From list
arr = np.array([1, 2, 3, 4])

# Special arrays
np.zeros(5)          # Array of zeros
np.ones(5)           # Array of ones
np.arange(0, 10, 2)  # Array with step
np.linspace(0, 1, 5) # 5 evenly spaced numbers
```

### Array Operations
```python
# Basic math (element-wise)
arr + 5              # Add 5 to each element
arr * 2              # Multiply each by 2
arr1 + arr2          # Element-wise addition

# Statistical operations
arr.mean()           # Mean
arr.sum()            # Sum
arr.std()            # Standard deviation
arr.min()            # Minimum
arr.max()            # Maximum
```

### Array Indexing & Slicing
```python
arr[0]               # First element
arr[-1]              # Last element
arr[1:4]             # Elements 1 to 3
arr[:3]              # First 3 elements
arr[arr > 5]         # Elements greater than 5
```

### Useful NumPy Functions
```python
np.where(condition)  # Find indices where condition is true
np.where(arr > 5, 1, 0)  # If-else vectorized
np.unique(arr)       # Unique values
np.concatenate([arr1, arr2])  # Join arrays
```

---

## 🔄 Common Data Transformations

### Type Conversion Best Practices
```python
# ALWAYS check types first
print(df.dtypes)
print(df.info())

# Clean and convert - Step by step
# Step 1: Check what you're dealing with
print(df['col'].head())
print(df['col'].dtype)

# Step 2: Clean if needed
df['col'] = df['col'].str.strip()  # Remove spaces
df['col'] = df['col'].str.replace(',', '')  # Remove commas

# Step 3: Convert safely
df['col'] = pd.to_numeric(df['col'], errors='coerce')

# Step 4: Verify
print(df['col'].dtype)  # Should be float64 or int64
print(df['col'].isnull().sum())  # Check how many failed
```

### String to Numeric Examples
```python
# Handle 'ESTRATO 1' -> 1
df['estrato'] = df['estrato'].str.replace('ESTRATO ', '').astype(int)

# Alternative: Extract numbers from string
df['estrato'] = df['estrato'].str.extract('(\d+)').astype(int)

# Handle currency '$1,234.56' -> 1234.56
df['price'] = df['price'].str.replace('[$,]', '', regex=True).astype(float)

# Handle percentages '85%' -> 0.85
df['rate'] = df['rate'].str.rstrip('%').astype(float) / 100

# Safe conversion with error handling
df['numeric_col'] = pd.to_numeric(df['col'], errors='coerce')
```

### Creating Categories
```python
# Using conditions
df['category'] = np.where(df['value'] > 5, 'High', 'Low')

# Multiple categories
conditions = [
    df['value'] < 3,
    df['value'] < 7,
    df['value'] >= 7
]
choices = ['Low', 'Medium', 'High']
df['category'] = np.select(conditions, choices)

# Using cut for bins
df['age_group'] = pd.cut(df['age'], bins=[0, 18, 65, 100], 
                         labels=['Child', 'Adult', 'Senior'])
```

### Date Operations
```python
# Convert to datetime
df['date'] = pd.to_datetime(df['date'])

# Extract components
df['year'] = df['date'].dt.year
df['month'] = df['date'].dt.month
df['day_of_week'] = df['date'].dt.dayofweek
```

---

## 📈 Quick Analysis Patterns

### Calculate Percentage
```python
# Percentage of total
(df['column'].value_counts() / len(df)) * 100

# Graduation rate example
graduation_rate = (df['graduated'] == 'SI').sum() / len(df) * 100
```

### Find Top/Bottom Performers
```python
# Top 5 by metric
top_5 = df.groupby('category')['metric'].mean().nlargest(5)

# Bottom 5
bottom_5 = df.groupby('category')['metric'].mean().nsmallest(5)
```

### Cross-tabulation
```python
# Count combinations
pd.crosstab(df['col1'], df['col2'])

# With percentages
pd.crosstab(df['col1'], df['col2'], normalize='index')
```

---

## 💾 Saving Results

### Export to CSV
```python
df.to_csv('output.csv', index=False)  # Without index
df.to_csv('output.csv', encoding='utf-8')  # With encoding
```

### Display Options
```python
pd.set_option('display.max_rows', 100)     # Show more rows
pd.set_option('display.max_columns', 50)   # Show more columns
pd.set_option('display.float_format', '{:.2f}'.format)  # Format decimals
```

---

## 🐛 Common Errors & Solutions

### TypeError: '>' not supported between 'str' and 'int'
**Solution**: Convert column to numeric first
```python
df['col'] = pd.to_numeric(df['col'], errors='coerce')
```

### TypeError: Cannot use method 'nlargest' with dtype object
**Solution**: Convert to numeric before using numeric methods
```python
# Check type first
print(df['col'].dtype)
# Convert to numeric
df['col'] = pd.to_numeric(df['col'], errors='coerce')
# Now you can use nlargest
df.nlargest(5, 'col')
```

### KeyError: 'column_name'
**Solution**: Check column exists
```python
df.columns  # List all columns
'column_name' in df.columns  # Check if exists
```

### ValueError: cannot convert string to float
**Solution**: Clean data before converting
```python
df['col'] = df['col'].str.replace(',', '')  # Remove commas
df['col'] = pd.to_numeric(df['col'], errors='coerce')
```

### SettingWithCopyWarning
**Solution**: Use `.copy()` or `.loc[]`
```python
subset = df[df['col'] > 5].copy()  # Create independent copy
df.loc[df['col'] > 5, 'new_col'] = value  # Proper assignment
```

---

## 🎯 Pro Tips

1. **Always check data types first**: Use `df.info()` before analysis
2. **Handle nulls early**: Clean data before calculations
3. **Use vectorization**: Avoid loops, use pandas/numpy operations
4. **Chain operations**: `df.groupby().agg().sort_values()`
5. **Keep original data**: Work on copies when transforming
6. **Verify results**: Check a few calculations manually
7. **Use meaningful names**: `graduation_rate` not `gr`
8. **Comment complex operations**: Explain why, not what

---

## 📚 Quick Reference Table

| Task | Pandas | NumPy |
|------|---------|--------|
| Read data | `pd.read_csv()` | - |
| Check shape | `df.shape` | `arr.shape` |
| First rows | `df.head()` | `arr[:5]` |
| Data types | `df.dtypes` | `arr.dtype` |
| Missing values | `df.isnull()` | `np.isnan()` |
| Mean | `df.mean()` | `arr.mean()` |
| Filter | `df[df['col'] > 5]` | `arr[arr > 5]` |
| Group by | `df.groupby()` | - |
| Sort | `df.sort_values()` | `np.sort()` |
| Unique | `df['col'].unique()` | `np.unique()` |

---

*Remember: Practice makes perfect! The more you use these commands, the more natural they become.*