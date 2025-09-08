# Exploratory Data Analysis (EDA) Workshop
## Colombian Pension Fund Dataset - Colfondos S.A.

---

## 🎯 Learning Objectives

By the end of this workshop, you will:
- Perform systematic EDA on real government data from datos.gov.co
- Apply the 4 fundamental steps of EDA methodology
- Generate actionable insights from pension fund investment data
- Practice data cleaning and visualization techniques
- Understand how to communicate findings for policy decisions

---

## 📊 Dataset Context

**What are we analyzing?**
- Investment portfolio data from **Colfondos S.A. Pensiones y Cesantías**
- One of Colombia's major pension fund administrators
- Dataset contains ~8,400 investment records with 112 variables
- Includes bonds, stocks, and other financial instruments

**Why is this important?**
- Pension funds manage retirement savings for millions of Colombians
- Understanding investment patterns ensures financial stability
- Regulatory compliance and risk management are critical
- Public policy implications for retirement security

---

## 🚀 Step 0: Environment Setup

Let's start by setting up our working environment.

### Task: Import Libraries and Configure Settings

```python
# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# Configuration for better display
warnings.filterwarnings('ignore')
pd.set_option('display.max_columns', 50)
pd.set_option('display.max_rows', 100)
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette('husl')

# Set figure size defaults
plt.rcParams['figure.figsize'] = (12, 6)
plt.rcParams['font.size'] = 12

print("✅ Environment setup complete!")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")
```

**💡 Tip:** Always start with a clean environment setup. This ensures reproducibility!

---

## 📥 Step 1: Data Loading and Initial Exploration

### 1.1 Load the Dataset

```python
# Load the dataset
df = pd.read_csv('Colfondos_20250830.csv')

# Get basic information
print("📊 Dataset Loaded Successfully!")
print("="*50)
print(f"Shape: {df.shape[0]:,} rows × {df.shape[1]} columns")
print(f"Memory usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
```

### 📝 **Question 1: Initial Observations**

Before continuing, write down your answers in a markdown cell:

1. **What do you think each row represents?**
   - Hint: Look at the column names and think about what a pension fund tracks

2. **Why might a pension fund have 8,400+ different investments?**
   - Think about: diversification, risk management, regulatory requirements

3. **What time period does this data cover?**
   - Look for date columns like 'Fecha de Corte'

```python
# Space for your answers
"""
My observations:
1. Each row represents: [Write your answer]
2. Diversification reason: [Write your answer]  
3. Time period: [Write your answer]
"""
```

### 1.2 Examine Column Names and Structure

```python
# Display first 20 columns to understand the structure
print("📋 First 20 Column Names:")
print("="*50)
for i, col in enumerate(df.columns[:20], 1):
    print(f"{i:2d}. {col}")

print("\n" + "="*50)
print(f"Total columns: {len(df.columns)}")
```

```python
# Check data types distribution
print("📊 Data Types Distribution:")
print("="*50)
dtype_counts = df.dtypes.value_counts()
for dtype, count in dtype_counts.items():
    print(f"{dtype}: {count} columns ({count/len(df.columns)*100:.1f}%)")
```

### 1.3 Preview the Data

```python
# Select important columns for initial viewing
important_cols = [
    'Nombre de Entidad', 
    'Fecha de Corte', 
    'Nombre Patrimonio',
    'Razon_Social_Emisor', 
    'Clase_Inversion',
    'Codigo_Moneda',
    'Valor_Mercado_O_Pres_Pesos'
]

# Check which columns exist in your dataset
existing_cols = [col for col in important_cols if col in df.columns]

print("🔍 Sample Data (First 5 rows):")
df[existing_cols].head()
```

**🤔 Think about:**
- What patterns do you notice in the issuer names (Razon_Social_Emisor)?
- Are there multiple currencies? What does this tell us?
- What investment classes appear most frequently?

---

## 🔍 Step 2: Data Quality Assessment

Good analysis requires good data. Let's check our data quality!

### 2.1 Missing Values Analysis

```python
# Calculate missing values
missing_data = pd.DataFrame({
    'Column': df.columns,
    'Missing_Count': df.isnull().sum(),
    'Missing_Percentage': (df.isnull().sum() / len(df)) * 100
})

# Filter columns with missing values
missing_data = missing_data[missing_data['Missing_Count'] > 0]
missing_data = missing_data.sort_values('Missing_Percentage', ascending=False)

print("🔍 Missing Values Analysis:")
print("="*50)
print(f"Columns with missing values: {len(missing_data)} out of {len(df.columns)}")
print(f"Total missing cells: {df.isnull().sum().sum():,}")
print(f"Percentage of dataset with missing values: {(df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100):.2f}%")

# Show top 10 columns with most missing values
print("\nTop 10 columns with missing values:")
print(missing_data.head(10))
```

### Visualize Missing Values Pattern

```python
# Create visualization of missing values
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Plot 1: Top 20 columns with most missing values
top_missing = missing_data.head(20)
ax1.barh(range(len(top_missing)), top_missing['Missing_Percentage'])
ax1.set_yticks(range(len(top_missing)))
ax1.set_yticklabels(top_missing['Column'], fontsize=8)
ax1.set_xlabel('Missing Percentage (%)')
ax1.set_title('Top 20 Columns with Missing Values')
ax1.grid(True, alpha=0.3)

# Plot 2: Distribution of missing values
missing_bins = [0, 10, 25, 50, 75, 100]
missing_labels = ['0-10%', '10-25%', '25-50%', '50-75%', '75-100%']
missing_data['Missing_Bin'] = pd.cut(
    missing_data['Missing_Percentage'], 
    bins=missing_bins, 
    labels=missing_labels
)
missing_dist = missing_data['Missing_Bin'].value_counts()

ax2.bar(range(len(missing_dist)), missing_dist.values)
ax2.set_xticks(range(len(missing_dist)))
ax2.set_xticklabels(missing_dist.index, rotation=45)
ax2.set_ylabel('Number of Columns')
ax2.set_xlabel('Missing Percentage Range')
ax2.set_title('Distribution of Missing Values Across Columns')
ax2.grid(True, alpha=0.3)

plt.tight_layout()
plt.show()
```

### 📝 **Question 2: Missing Data Patterns**

Analyze the missing values and answer:

1. **Why might certain financial fields have missing values?**
   - Consider: Different instrument types might not need all fields

2. **Could missing values indicate different types of investments?**
   - Example: Stock fields might be null for bonds

3. **Should we remove columns with >50% missing values? Why or why not?**
   - Think about: Information value vs. noise

```python
# Your analysis here
"""
Missing data insights:
1. Reason for missing values: [Your answer]
2. Investment type indication: [Your answer]
3. Removal strategy: [Your answer]
"""
```

### 2.2 Duplicate Detection

```python
# Check for duplicate rows
duplicates = df.duplicated().sum()
print("🔍 Duplicate Analysis:")
print("="*50)
print(f"Number of duplicate rows: {duplicates:,}")
print(f"Percentage of duplicates: {(duplicates/len(df))*100:.2f}%")

# Check for duplicates based on key columns
key_columns = ['Nro_Asignado_Por_La_Entidad', 'Fecha de Corte']
existing_key_cols = [col for col in key_columns if col in df.columns]

if existing_key_cols:
    key_duplicates = df.duplicated(subset=existing_key_cols).sum()
    print(f"\nDuplicates based on {existing_key_cols}: {key_duplicates:,}")
```

### 2.3 Data Type Corrections

```python
# Identify columns that should be numeric but aren't
print("🔧 Data Type Analysis:")
print("="*50)

# Columns that likely should be numeric
potential_numeric = [
    'Valor Nominal', 
    'Valor_Mercado_O_Pres_Pesos', 
    'Vr. presente en $',
    'Tasa de negociacion', 
    'Días al v/to', 
    'Precio'
]

for col in potential_numeric:
    if col in df.columns:
        dtype = df[col].dtype
        if dtype == 'object':
            print(f"⚠️  '{col}' is type '{dtype}' - converting to numeric...")
            # Clean and convert
            df[col] = pd.to_numeric(
                df[col].astype(str).str.replace(',', ''), 
                errors='coerce'
            )
```

---

## 📊 Step 3: Univariate Analysis

Let's analyze individual variables to understand their distributions.

### 3.1 Categorical Variables Analysis

#### Investment Classes Distribution

```python
# Analyze investment classes
if 'Clase_Inversion' in df.columns:
    print("📊 Investment Classes Distribution:")
    print("="*50)
    investment_classes = df['Clase_Inversion'].value_counts()
    print(f"Number of unique investment classes: {len(investment_classes)}")
    print("\nTop 10 Investment Classes:")
    print(investment_classes.head(10))
    
    # Visualization
    fig, ax = plt.subplots(figsize=(12, 6))
    investment_classes.head(15).plot(kind='barh', ax=ax, color='steelblue')
    ax.set_xlabel('Number of Holdings')
    ax.set_title('Top 15 Investment Classes by Number of Holdings')
    ax.grid(True, alpha=0.3)
    
    # Add value labels
    for i, v in enumerate(investment_classes.head(15).values):
        ax.text(v + 10, i, str(v), va='center')
    
    plt.tight_layout()
    plt.show()
```

#### Currency Distribution

```python
# Analyze currencies
if 'Codigo_Moneda' in df.columns:
    print("💱 Currency Distribution:")
    print("="*50)
    currencies = df['Codigo_Moneda'].value_counts()
    print(f"Number of different currencies: {len(currencies)}")
    print("\nCurrency breakdown:")
    for currency, count in currencies.items():
        print(f"  {currency}: {count:,} ({count/len(df)*100:.2f}%)")
    
    # Pie chart visualization
    fig, ax = plt.subplots(figsize=(10, 8))
    colors = plt.cm.Set3(range(len(currencies)))
    currencies.plot(kind='pie', autopct='%1.1f%%', ax=ax, colors=colors)
    ax.set_ylabel('')
    ax.set_title('Investment Distribution by Currency', fontsize=16)
    plt.show()
```

### 📝 **Question 3: Currency Diversification**

Based on the currency distribution:

1. **What does the currency mix tell us about the fund's risk strategy?**
2. **Why might a Colombian pension fund invest in foreign currencies?**
3. **What risks does this currency exposure create?**

```python
# Your insights
"""
Currency analysis:
1. Risk strategy insight: [Your answer]
2. Reason for foreign investment: [Your answer]
3. Currency risk exposure: [Your answer]
"""
```

### 3.2 Numerical Variables Analysis

```python
# Convert and analyze market values
if 'Valor_Mercado_O_Pres_Pesos' in df.columns:
    # Create clean numeric column
    df['Market_Value_Clean'] = pd.to_numeric(
        df['Valor_Mercado_O_Pres_Pesos'].astype(str).str.replace(',', ''),
        errors='coerce'
    )
    
    print("💰 Market Value Analysis:")
    print("="*50)
    print(df['Market_Value_Clean'].describe())
    
    # Portfolio metrics
    total_portfolio = df['Market_Value_Clean'].sum()
    print(f"\nTotal Portfolio Value: ${total_portfolio:,.2f} COP")
    print(f"Total Portfolio Value: ${total_portfolio/1e12:.2f} Trillion COP")
    
    # Concentration analysis
    top_10_holdings = df.nlargest(10, 'Market_Value_Clean')
    top_10_value = top_10_holdings['Market_Value_Clean'].sum()
    print(f"\nTop 10 holdings represent {top_10_value/total_portfolio*100:.2f}% of portfolio")
```

### Distribution Visualizations

```python
# Create comprehensive distribution analysis
if 'Market_Value_Clean' in df.columns:
    fig, axes = plt.subplots(2, 2, figsize=(15, 10))
    
    # 1. Histogram with log scale
    axes[0, 0].hist(df['Market_Value_Clean'].dropna(), bins=50, 
                    edgecolor='black', color='skyblue')
    axes[0, 0].set_xlabel('Market Value (COP)')
    axes[0, 0].set_ylabel('Frequency')
    axes[0, 0].set_title('Distribution of Investment Values')
    axes[0, 0].set_yscale('log')
    
    # 2. Box plot
    axes[0, 1].boxplot(df['Market_Value_Clean'].dropna())
    axes[0, 1].set_ylabel('Market Value (COP)')
    axes[0, 1].set_title('Investment Value Box Plot (Shows Outliers)')
    axes[0, 1].set_yscale('log')
    
    # 3. Top 20 holdings bar chart
    top_20 = df.nlargest(20, 'Market_Value_Clean')
    axes[1, 0].barh(range(len(top_20)), top_20['Market_Value_Clean'].values)
    axes[1, 0].set_yticks(range(len(top_20)))
    axes[1, 0].set_yticklabels(
        [str(x)[:30] for x in top_20['Razon_Social_Emisor'].values], 
        fontsize=8
    )
    axes[1, 0].set_xlabel('Market Value (COP)')
    axes[1, 0].set_title('Top 20 Holdings by Value')
    
    # 4. Cumulative distribution (Lorenz curve)
    sorted_values = df['Market_Value_Clean'].dropna().sort_values(ascending=False)
    cumsum = sorted_values.cumsum() / sorted_values.sum() * 100
    axes[1, 1].plot(range(len(cumsum)), cumsum.values, linewidth=2)
    axes[1, 1].axhline(y=80, color='r', linestyle='--', label='80% of portfolio')
    axes[1, 1].set_xlabel('Number of Holdings')
    axes[1, 1].set_ylabel('Cumulative % of Portfolio')
    axes[1, 1].set_title('Portfolio Concentration Curve')
    axes[1, 1].legend()
    axes[1, 1].grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.show()
```

**💡 Insight Check:** 
- How many investments make up 50% of the portfolio value?
- What does this tell us about concentration risk?

---

## 🔗 Step 4: Bivariate Analysis

Now let's explore relationships between variables.

### 4.1 Investment Type vs Value Analysis

```python
# Analyze investment value by class
if 'Clase_Inversion' in df.columns and 'Market_Value_Clean' in df.columns:
    investment_summary = df.groupby('Clase_Inversion').agg({
        'Market_Value_Clean': ['sum', 'mean', 'count']
    }).round(2)
    
    investment_summary.columns = ['Total_Value', 'Avg_Value', 'Count']
    investment_summary['Pct_Portfolio'] = (
        investment_summary['Total_Value'] / 
        investment_summary['Total_Value'].sum() * 100
    ).round(2)
    investment_summary = investment_summary.sort_values('Total_Value', ascending=False)
    
    print("📊 Investment Summary by Class:")
    print("="*80)
    print(investment_summary.head(10))
```

### Visualization: Investment Class Analysis

```python
# Create dual visualization
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Total value by class
top_classes = investment_summary.head(10)
bars = ax1.bar(range(len(top_classes)), top_classes['Total_Value'].values, 
               color='steelblue')
ax1.set_xticks(range(len(top_classes)))
ax1.set_xticklabels([str(x)[:15] for x in top_classes.index], 
                     rotation=45, ha='right')
ax1.set_ylabel('Total Value (COP)')
ax1.set_title('Top 10 Investment Classes by Total Value')
ax1.grid(True, alpha=0.3)

# Average value vs count (bubble chart)
scatter = ax2.scatter(top_classes['Count'], 
                     top_classes['Avg_Value'],
                     s=top_classes['Pct_Portfolio']*50, 
                     alpha=0.6,
                     c=range(len(top_classes)),
                     cmap='viridis')
ax2.set_xlabel('Number of Holdings')
ax2.set_ylabel('Average Value per Holding (COP)')
ax2.set_title('Investment Class Characteristics\n(Bubble size = % of portfolio)')
ax2.grid(True, alpha=0.3)

# Add labels to bubbles
for idx, row in top_classes.iterrows():
    ax2.annotate(str(idx)[:10], 
                (row['Count'], row['Avg_Value']),
                fontsize=8, alpha=0.7)

plt.tight_layout()
plt.show()
```

### 📝 **Question 4: Portfolio Strategy**

Based on the investment class analysis:

1. **Which investment classes dominate the portfolio?**
2. **Is the fund taking a concentrated or diversified approach?**
3. **What does the average value per holding tell us about investment strategy?**

```python
# Your analysis
"""
Portfolio strategy insights:
1. Dominant investment classes: [Your answer]
2. Concentration vs diversification: [Your answer]
3. Investment strategy insight: [Your answer]
"""
```

### 4.2 Country Risk Analysis

```python
# Analyze investments by country
if 'Pais_Emisor' in df.columns and 'Market_Value_Clean' in df.columns:
    country_analysis = df.groupby('Pais_Emisor').agg({
        'Market_Value_Clean': ['sum', 'count', 'mean']
    }).round(2)
    
    country_analysis.columns = ['Total_Value', 'Num_Investments', 'Avg_Investment']
    country_analysis['Pct_Portfolio'] = (
        country_analysis['Total_Value'] / 
        country_analysis['Total_Value'].sum() * 100
    ).round(2)
    country_analysis = country_analysis.sort_values('Total_Value', ascending=False)
    
    print("🌍 Geographic Distribution of Investments:")
    print("="*80)
    print(country_analysis.head(15))
```

### Geographic Distribution Visualization

```python
# Create geographic distribution chart
fig, ax = plt.subplots(figsize=(12, 8))

top_countries = country_analysis.head(15)
colors = plt.cm.Set3(np.linspace(0, 1, len(top_countries)))

bars = ax.bar(range(len(top_countries)), 
              top_countries['Pct_Portfolio'].values, 
              color=colors)
ax.set_xticks(range(len(top_countries)))
ax.set_xticklabels(top_countries.index, rotation=45, ha='right')
ax.set_ylabel('% of Total Portfolio')
ax.set_title('Geographic Distribution of Pension Fund Investments', fontsize=16)
ax.grid(True, alpha=0.3, axis='y')

# Add value labels on bars
for i, (bar, val) in enumerate(zip(bars, top_countries['Pct_Portfolio'].values)):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
            f'{val:.1f}%', ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.show()
```

---

## 🌐 Step 5: Multivariate Analysis

Let's analyze multiple variables simultaneously to find complex patterns.

### 5.1 Investment Class × Currency Analysis

```python
# Multi-dimensional analysis
if all(col in df.columns for col in ['Clase_Inversion', 'Codigo_Moneda', 'Market_Value_Clean']):
    # Create pivot table
    pivot_data = df.pivot_table(
        values='Market_Value_Clean',
        index='Clase_Inversion',
        columns='Codigo_Moneda',
        aggfunc='sum',
        fill_value=0
    )
    
    # Select top classes for visualization
    top_classes = pivot_data.sum(axis=1).nlargest(10).index
    pivot_subset = pivot_data.loc[top_classes]
    
    # Create heatmap
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(pivot_subset, 
                annot=False, 
                fmt='.0f', 
                cmap='YlOrRd',
                cbar_kws={'label': 'Total Investment Value (COP)'})
    ax.set_title('Investment Heatmap: Class vs Currency', fontsize=16)
    ax.set_xlabel('Currency')
    ax.set_ylabel('Investment Class')
    plt.tight_layout()
    plt.show()
```

### 5.2 Portfolio Segmentation

```python
# Create investment segments based on value
if 'Market_Value_Clean' in df.columns:
    # Define segments
    df['Investment_Segment'] = pd.cut(
        df['Market_Value_Clean'],
        bins=[0, 1e9, 10e9, 50e9, 100e9, float('inf')],
        labels=['Small (<1B)', 'Medium (1-10B)', 'Large (10-50B)', 
                'Very Large (50-100B)', 'Mega (>100B)']
    )
    
    # Analyze segments
    segment_analysis = df.groupby('Investment_Segment').agg({
        'Market_Value_Clean': ['count', 'sum', 'mean']
    }).round(2)
    
    segment_analysis.columns = ['Count', 'Total_Value', 'Avg_Value']
    segment_analysis['Pct_Count'] = (
        segment_analysis['Count'] / segment_analysis['Count'].sum() * 100
    ).round(2)
    segment_analysis['Pct_Value'] = (
        segment_analysis['Total_Value'] / segment_analysis['Total_Value'].sum() * 100
    ).round(2)
    
    print("📊 Portfolio Segmentation Analysis:")
    print("="*80)
    print(segment_analysis)
```

### Segment Distribution Visualization

```python
# Create comparative pie charts
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# Distribution by count
segment_analysis['Pct_Count'].plot(kind='pie', ax=ax1, autopct='%1.1f%%',
                                   colors=plt.cm.Set3.colors)
ax1.set_title('Distribution of Investments by Count')
ax1.set_ylabel('')

# Distribution by value
segment_analysis['Pct_Value'].plot(kind='pie', ax=ax2, autopct='%1.1f%%',
                                   colors=plt.cm.Set3.colors)
ax2.set_title('Distribution of Portfolio Value')
ax2.set_ylabel('')

plt.tight_layout()
plt.show()
```

### 📝 **Question 5: Portfolio Concentration Risk**

Based on the segmentation analysis:

1. **How concentrated is the portfolio? Is this healthy?**
2. **What percentage of holdings represent 80% of the portfolio value?**
3. **What are the implications for risk management?**

```python
# Your risk assessment
"""
Risk assessment:
1. Concentration level: [Your answer]
2. 80% portfolio concentration: [Your answer]
3. Risk management implications: [Your answer]
"""
```

---

## 📈 Step 6: Key Performance Indicators (KPIs)

Let's calculate and display critical metrics for decision-making.

```python
# Calculate comprehensive KPIs
print("📈 Key Performance Indicators (KPIs):")
print("="*80)

if 'Market_Value_Clean' in df.columns:
    # Basic metrics
    total_portfolio = df['Market_Value_Clean'].sum()
    num_investments = len(df)
    avg_investment = df['Market_Value_Clean'].mean()
    median_investment = df['Market_Value_Clean'].median()
    
    # Concentration metrics
    top_10_pct = (df.nlargest(10, 'Market_Value_Clean')['Market_Value_Clean'].sum() / 
                  total_portfolio * 100)
    top_50_pct = (df.nlargest(50, 'Market_Value_Clean')['Market_Value_Clean'].sum() / 
                  total_portfolio * 100)
    
    # Find how many holdings make up 80% of portfolio
    sorted_values = df['Market_Value_Clean'].sort_values(ascending=False)
    cumsum_pct = sorted_values.cumsum() / total_portfolio * 100
    holdings_for_80pct = (cumsum_pct <= 80).sum()
    
    # Diversification metrics
    num_currencies = df['Codigo_Moneda'].nunique() if 'Codigo_Moneda' in df.columns else 'N/A'
    num_countries = df['Pais_Emisor'].nunique() if 'Pais_Emisor' in df.columns else 'N/A'
    num_investment_classes = df['Clase_Inversion'].nunique() if 'Clase_Inversion' in df.columns else 'N/A'
    
    # Display KPIs
    print("\n📊 PORTFOLIO METRICS:")
    print(f"  • Total Portfolio Value: ${total_portfolio:,.0f} COP")
    print(f"  • Total Portfolio Value: ${total_portfolio/1e12:.2f} Trillion COP")
    print(f"  • Number of Investments: {num_investments:,}")
    print(f"  • Average Investment Size: ${avg_investment:,.0f} COP")
    print(f"  • Median Investment Size: ${median_investment:,.0f} COP")
    
    print("\n⚠️  CONCENTRATION METRICS:")
    print(f"  • Top 10 Holdings: {top_10_pct:.2f}% of portfolio")
    print(f"  • Top 50 Holdings: {top_50_pct:.2f}% of portfolio")
    print(f"  • Holdings for 80% of value: {holdings_for_80pct} investments")
    
    print("\n🌍 DIVERSIFICATION METRICS:")
    print(f"  • Number of Currencies: {num_currencies}")
    print(f"  • Number of Countries: {num_countries}")
    print(f"  • Number of Investment Classes: {num_investment_classes}")
```

---

## 💡 Step 7: Generate Business Insights

Let's automatically generate insights based on our analysis.

```python
# Generate automated insights
print("💡 Key Insights from EDA:")
print("="*80)

insights = []

# Insight 1: Portfolio concentration
if top_10_pct > 50:
    insights.append(f"⚠️ HIGH CONCENTRATION RISK: Top 10 holdings = {top_10_pct:.1f}% of portfolio")
elif top_10_pct > 30:
    insights.append(f"📊 MODERATE CONCENTRATION: Top 10 holdings = {top_10_pct:.1f}% of portfolio")
else:
    insights.append(f"✅ WELL DIVERSIFIED: Top 10 holdings = {top_10_pct:.1f}% of portfolio")

# Insight 2: Currency exposure
if 'Codigo_Moneda' in df.columns and 'Market_Value_Clean' in df.columns:
    foreign_exposure = (df[df['Codigo_Moneda'] != 'COP']['Market_Value_Clean'].sum() / 
                       total_portfolio * 100)
    if foreign_exposure > 40:
        insights.append(f"🌍 HIGH FOREIGN EXPOSURE: {foreign_exposure:.1f}% in foreign currencies")
    else:
        insights.append(f"🏠 DOMESTIC FOCUSED: {100-foreign_exposure:.1f}% in Colombian Pesos")

# Insight 3: Investment efficiency
if avg_investment > median_investment * 10:
    insights.append("📈 HIGHLY SKEWED: Few large investments dominate")
else:
    insights.append("📊 BALANCED: Investment sizes are relatively uniform")

# Insight 4: Data quality
missing_pct = (df.isnull().sum().sum() / (df.shape[0] * df.shape[1]) * 100)
if missing_pct > 30:
    insights.append(f"⚠️ DATA QUALITY ISSUE: {missing_pct:.1f}% missing data")
else:
    insights.append(f"✅ GOOD DATA QUALITY: Only {missing_pct:.1f}% missing data")

# Insight 5: Portfolio complexity
if num_investments > 5000:
    insights.append(f"🔄 COMPLEX PORTFOLIO: Managing {num_investments:,} positions")
else:
    insights.append(f"📋 MANAGEABLE PORTFOLIO: {num_investments:,} positions")

# Display insights
print("\n🎯 TOP 5 INSIGHTS:\n")
for i, insight in enumerate(insights, 1):
    print(f"{i}. {insight}")
```

---

## 📝 Step 8: Final Exercise - Policy Recommendations

### Your Turn: Generate 5 Policy Recommendations

Based on your complete EDA, provide **5 specific, actionable recommendations** for:

1. **Risk Management Improvements**
   - What concentration limits should be implemented?
   - How can the fund better manage currency risk?

2. **Portfolio Optimization Strategies**
   - Which asset classes should be increased/decreased?
   - What rebalancing strategies would improve returns?

3. **Regulatory Compliance Considerations**
   - Are there regulatory limits being approached?
   - What monitoring systems should be implemented?

4. **Data Collection Improvements**
   - Which data fields need better quality control?
   - What additional data would enhance analysis?

5. **Future Analysis Priorities**
   - What deeper analyses should be conducted?
   - Which patterns require further investigation?

```python
# Template for your recommendations
recommendations = """
POLICY RECOMMENDATIONS FOR COLFONDOS S.A.
==========================================

1. RISK MANAGEMENT:
   • [Your specific recommendation]
   • Expected impact: [Quantify if possible]
   • Implementation timeline: [Immediate/Short-term/Long-term]

2. PORTFOLIO OPTIMIZATION:
   • [Your specific recommendation]
   • Expected impact: [Quantify if possible]
   • Implementation timeline: [Immediate/Short-term/Long-term]

3. REGULATORY COMPLIANCE:
   • [Your specific recommendation]
   • Expected impact: [Quantify if possible]
   • Implementation timeline: [Immediate/Short-term/Long-term]

4. DATA QUALITY:
   • [Your specific recommendation]
   • Expected impact: [Quantify if possible]
   • Implementation timeline: [Immediate/Short-term/Long-term]

5. FUTURE ANALYSIS:
   • [Your specific recommendation]
   • Expected impact: [Quantify if possible]
   • Implementation timeline: [Immediate/Short-term/Long-term]

EXPECTED OVERALL IMPACT:
[Describe the combined benefits of implementing all recommendations]
"""

print(recommendations)
```

---

## 📊 Step 9: Create Executive Summary

```python
# Generate executive summary
executive_summary = f"""
EXECUTIVE SUMMARY - COLFONDOS PORTFOLIO ANALYSIS
================================================

Date: {pd.Timestamp.now().strftime('%Y-%m-%d')}
Dataset: Colfondos_20250830.csv

KEY METRICS:
• Portfolio Value: ${total_portfolio/1e12:.2f} Trillion COP
• Total Investments: {num_investments:,}
• Geographic Reach: {num_countries} countries
• Currency Exposure: {num_currencies} currencies

RISK PROFILE:
• Concentration: Top 10 holdings = {top_10_pct:.1f}% of portfolio
• Foreign Exposure: {foreign_exposure:.1f}%
• Data Quality Score: {100 - missing_pct:.1f}%

TOP 3 PRIORITIES:
1. {insights[0]}
2. {insights[1]}
3. {insights[2]}

RECOMMENDATION:
[Your main recommendation based on the analysis]
"""

print(executive_summary)
```

---

## 🎯 Workshop Summary

### What We've Accomplished:

✅ **Loaded and explored** a complex financial dataset with 8,400+ records  
✅ **Assessed data quality** identifying patterns in missing values  
✅ **Performed univariate analysis** on key variables  
✅ **Conducted bivariate analysis** to find relationships  
✅ **Applied multivariate techniques** for deeper insights  
✅ **Generated KPIs** for executive decision-making  
✅ **Created actionable recommendations** based on evidence  

### Key Takeaways:

1. **Systematic EDA is crucial** - Follow a structured approach
2. **Data quality matters** - Clean data leads to reliable insights
3. **Visualization communicates** - Charts reveal patterns numbers hide
4. **Context is king** - Domain knowledge enhances interpretation
5. **Insights drive action** - Analysis without recommendations is incomplete

### Skills You've Developed:

- 📊 Data profiling and quality assessment
- 📈 Statistical analysis and interpretation
- 🎨 Effective data visualization
- 💡 Pattern recognition and anomaly detection
- 📝 Business insight generation
- 🎯 Strategic recommendation formulation

---

## 🚀 Next Steps

### Continue Your Learning:

1. **Practice with Different Datasets**
   - Try other datos.gov.co datasets
   - Apply the same methodology
   - Compare patterns across sectors

2. **Advanced Techniques**
   - Learn correlation analysis
   - Explore time series decomposition
   - Study outlier detection methods

3. **Automation**
   - Create reusable EDA functions
   - Build automated reporting pipelines
   - Develop data quality monitoring

4. **Visualization Mastery**
   - Learn interactive visualizations (Plotly, Bokeh)
   - Create dashboards (Streamlit, Dash)
   - Master storytelling with data

5. **Machine Learning Connection**
   - Use EDA findings for feature engineering
   - Identify target variables for prediction
   - Understand data requirements for ML models

---

## 📚 Additional Resources

### Recommended Reading:
- "Exploratory Data Analysis" by John Tukey
- "The Visual Display of Quantitative Information" by Edward Tufte
- "Storytelling with Data" by Cole Nussbaumer Knaflic

### Online Resources:
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Seaborn Gallery](https://seaborn.pydata.org/examples/index.html)
- [Colombia Open Data Portal](https://www.datos.gov.co/)

### Practice Datasets:
- Financial market data from Banco de la República
- Economic indicators from DANE
- Public procurement data from Colombia Compra Eficiente

---

## 🎉 Congratulations!

You've completed a comprehensive EDA on real Colombian pension fund data!

**Remember:**
- Every dataset tells a story
- Good analysis leads to better decisions
- Practice makes perfect
- Always question your findings
- Share your insights to create impact

### Final Challenge:
Can you find one pattern in the data that we didn't explore? What question would you ask next?

---

**Happy Analyzing! 🚀**

*"In God we trust, all others must bring data."* - W. Edwards Deming