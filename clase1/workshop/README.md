# 📊 Data Analytics Workshop: Financial Statements Analysis
## Introduction to Data Analytics - Class 1

### ⏰ Duration: 1 hour 30 minutes
### 💻 Tool: Jupyter Notebook
### 📝 Dataset: Colombian Entity Financial Statements

---

## 🎯 Workshop Overview

This workshop introduces fundamental data analytics concepts through hands-on analysis of real financial data. You'll learn to transform raw data into actionable business insights using Python and Jupyter notebooks.

### Learning Objectives
By the end of this workshop, you will:
- ✅ Understand the Data → Information → Knowledge transformation model
- ✅ Load and explore real financial data using pandas
- ✅ Create meaningful visualizations with matplotlib
- ✅ Generate actionable insights from data analysis
- ✅ Build a basic financial dashboard

---

## 📚 Key Concepts

### The Data Analytics Pipeline

```
📦 RAW DATA                 📈 INFORMATION              🧠 KNOWLEDGE
Numbers without      →      Processed &           →     Insights for
context                     organized data              decision-making

Example:
$650,460,896,321    →      Assets: $650B         →     "High liquidity 
                           Cash: 44%                    position - consider
                                                       investments"
```

### Financial Statements Basics

**Balance Sheet (Estado de Situación Financiera)**
- **Assets (Activos)**: What the company owns
- **Liabilities (Pasivos)**: What the company owes  
- **Equity (Patrimonio)**: Net worth

**Income Statement (Estado de Resultados)**
- **Revenue (Ingresos)**: Money earned
- **Expenses (Gastos)**: Money spent
- **Profit/Loss (Utilidad/Pérdida)**: The difference

---

## 🚀 Getting Started

### 🐍 What is a Virtual Environment (venv)?

A **virtual environment** is an isolated Python environment that allows you to install packages without affecting your system's Python installation. Think of it as a "sandbox" for your project.

#### Why Use Virtual Environments?
- ✅ **Isolation**: Each project has its own dependencies
- ✅ **No Conflicts**: Avoid version conflicts between projects
- ✅ **Clean System**: Keep your main Python installation clean
- ✅ **Reproducibility**: Easy to share exact package versions

### 📦 Environment Setup (IMPORTANT - Do This First!)

#### Step 1: Create Virtual Environment

**For Windows:**
```cmd
# Navigate to the workshop folder
cd path\to\workshop\folder

# Create virtual environment
python -m venv data_analytics_env

# Activate the environment
data_analytics_env\Scripts\activate
```

**For macOS/Linux:**
```bash
# Navigate to the workshop folder
cd path/to/workshop/folder

# Create virtual environment
python3 -m venv data_analytics_env

# Activate the environment
source data_analytics_env/bin/activate
```

#### Step 2: Install Required Packages

Once your virtual environment is activated (you'll see `(data_analytics_env)` in your terminal), install the packages:

```bash
# Install all required packages at once
pip install -r requirements.txt

# OR install packages individually:
pip install pandas numpy matplotlib seaborn jupyter notebook plotly openpyxl
```

#### Step 3: Start Jupyter Notebook

```bash
# Launch Jupyter Notebook
jupyter notebook

# OR launch Jupyter Lab (more modern interface)
jupyter lab
```

#### Step 4: Verify Installation

Create a test cell in a new notebook and run:
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
print("✅ All packages installed successfully!")
```

### 🔧 How to Deactivate Virtual Environment

When you're done with the workshop:
```bash
# Deactivate the virtual environment
deactivate
```

### Files Needed
1. `requirements.txt` - Package dependencies (provided)
2. `Estados_Financieros___Estado_de_Resultados_y_Estado_de_Situaci_n_Financiera_20250809.csv` - The dataset
3. `financial_analysis_workshop.ipynb` - The notebook you'll create
4. `README.md` - This guide

---

## 📖 Workshop Structure

The workshop is divided into 5 main parts:

### Part 1: Setup & Data Loading (15 min)
- Import libraries
- Load the CSV file
- Initial data exploration

### Part 2: Data Exploration (15 min)
- Understand data structure
- Identify data types
- Explore categories

### Part 3: Information Processing (20 min)
- Separate financial statements
- Calculate key metrics
- Create basic visualizations

### Part 4: Knowledge Generation (25 min)
- Analyze financial health
- Identify patterns
- Build executive dashboard

### Part 5: Your Analysis (15 min)
- Custom insights
- Recommendations
- Conclusions

---

## 📝 Step-by-Step Instructions

### 🔧 PART 1: ENVIRONMENT SETUP

#### What You'll Learn
- How to set up a data analysis environment
- Importing essential Python libraries
- Creating helper functions for data formatting

#### Instructions

1. **Create a new Jupyter notebook** named `financial_analysis_workshop.ipynb`

2. **Add a title cell** (Markdown):
   - Click on the first cell
   - Change to Markdown (dropdown menu)
   - Add your title and information

3. **Import libraries** (Code cell):
   - Copy the import statements
   - Run the cell (Shift + Enter)
   - Verify all libraries load correctly

4. **Create helper functions**:
   - These will format large numbers
   - Make output more readable

#### Expected Output
✅ "Libraries imported successfully!" message  
✅ Pandas version displayed  
✅ Helper functions ready to use

---

### 📥 PART 2: DATA EXPLORATION

#### What You'll Learn
- Loading data from CSV files
- Understanding data structure
- Identifying data quality issues
- Basic pandas operations

#### Instructions

1. **Load the dataset**:
   - Use `pd.read_csv()` function
   - Store in variable `df`
   - Check dimensions with `.shape`

2. **Explore the structure**:
   - Use `.head()` to see first rows
   - Use `.info()` for data types
   - Use `.columns` to list all columns

3. **Understand categories**:
   - Find unique values in 'Tipo de Estado'
   - Count records per category
   - Identify main account types

#### Key Questions to Answer
- How many rows and columns does the dataset have?
- What types of financial statements are included?
- What are the main categories in the data?

#### Expected Output
✅ Dataset dimensions displayed  
✅ Column names and types listed  
✅ Categories identified and counted

---

### 📊 PART 3: INFORMATION PROCESSING

#### What You'll Learn
- Data filtering and grouping
- Calculating financial metrics
- Creating meaningful visualizations
- Using pandas aggregation functions

#### Instructions

1. **Separate financial statements**:
   ```python
   # Filter for Balance Sheet
   balance_sheet = df[df['Tipo de Estado'] == 'Estado de Situación Financiera']
   
   # Filter for Income Statement  
   income_statement = df[df['Tipo de Estado'] == 'Estado de Resultados']
   ```

2. **Calculate key metrics**:
   - Total assets
   - Cash and equivalents
   - Liquidity ratio (Cash/Assets)

3. **Create visualizations**:
   - Bar chart of top asset components
   - Pie chart of category distribution
   - Use matplotlib and seaborn

#### Analysis Focus
- What percentage of assets is liquid?
- Which are the largest asset components?
- How are resources distributed across categories?

#### Expected Output
✅ Separated datasets for each statement  
✅ Key financial metrics calculated  
✅ 2-3 clear visualizations created

---

### 🧠 PART 4: KNOWLEDGE GENERATION

#### What You'll Learn
- Interpreting financial indicators
- Identifying patterns and trends
- Creating executive dashboards
- Generating actionable insights

#### Instructions

1. **Analyze financial health**:
   - Evaluate liquidity position
   - Identify risk indicators (provisions)
   - Assess investment strategy

2. **Create insights**:
   ```python
   if liquidity_ratio > 30:
       insight = "Strong liquidity - consider investments"
   elif liquidity_ratio > 15:
       insight = "Adequate liquidity - monitor closely"
   else:
       insight = "Low liquidity - needs attention"
   ```

3. **Build executive dashboard**:
   - Combine multiple visualizations
   - Add key metrics summary
   - Include recommendations

#### Key Insights to Generate
- Is the organization financially healthy?
- What are the main risks?
- What actions should management take?

#### Expected Output
✅ Financial health assessment  
✅ 3-5 actionable insights  
✅ Executive dashboard with 4+ components

---

### 💡 PART 5: YOUR ANALYSIS

#### What You'll Learn
- Independent data exploration
- Creative problem-solving
- Business recommendation writing
- Presenting findings effectively

#### Instructions

1. **Choose your focus**:
   - Pick an interesting aspect of the data
   - Examples: debt analysis, investment portfolio, operational efficiency

2. **Perform analysis**:
   - Filter relevant data
   - Calculate new metrics
   - Create custom visualization

3. **Write recommendations**:
   - Short-term actions (0-3 months)
   - Medium-term plans (3-12 months)
   - Long-term strategy (1+ years)

#### Deliverables
✅ One custom analysis with visualization  
✅ Three strategic recommendations  
✅ Brief executive summary

---

## 💭 Reflection Questions

After each part, answer these questions in markdown cells:

### After Part 2: Data Exploration
> "Looking at the raw data, can you understand the financial position? Why or why not?"

### After Part 3: Information Processing
> "How did organizing and visualizing help you understand the data better?"

### After Part 4: Knowledge Generation
> "What are the THREE most important insights you discovered?"

### After Part 5: Your Analysis
> "If you were the CFO, what decision would you make based on this analysis?"

---

## 📊 Code Templates

### Loading Data
```python
import pandas as pd
df = pd.read_csv('your_file.csv')
print(f"Loaded {len(df)} records")
```

### Basic Filtering
```python
filtered_df = df[df['column'] == 'value']
```

### Grouping and Aggregation
```python
summary = df.groupby('category')['value'].sum()
```

### Simple Visualization
```python
import matplotlib.pyplot as plt
plt.figure(figsize=(10, 6))
plt.bar(x_values, y_values)
plt.title('Your Title')
plt.show()
```

---

## 🎯 Success Criteria

Your completed notebook should have:

| Component | Requirement | Points |
|-----------|------------|--------|
| Code Cells | 15+ executed cells | 30 |
| Visualizations | 4+ charts/graphs | 20 |
| Insights | 3+ actionable insights | 20 |
| Recommendations | Strategic plan provided | 15 |
| Reflection | All questions answered | 15 |
| **Total** | | **100** |

---

## 🚨 Common Issues & Solutions

### Virtual Environment Issues

#### Issue: "Command 'python' not found" (Linux/Mac)
**Solution**: Use `python3` instead of `python`:
```bash
python3 -m venv data_analytics_env
```

#### Issue: Virtual environment not activating
**Solution**: 
- **Windows**: Make sure you're using `Scripts\activate` (not `bin/activate`)
- **Mac/Linux**: Make sure you're using `source` before the path
- Check if you're in the correct directory

#### Issue: "pip: command not found" 
**Solution**: 
```bash
# Try upgrading pip first
python -m ensurepip --upgrade
# OR
python -m pip install --upgrade pip
```

#### Issue: Permission denied when installing packages
**Solution**: 
```bash
# Never use sudo with virtual environments!
# Instead, make sure your venv is activated:
# You should see (data_analytics_env) in your prompt

# If still issues, try:
pip install --user -r requirements.txt
```

### Package Installation Issues

#### Issue: "Module not found" after installation
**Solutions**:
1. Make sure virtual environment is activated
2. Restart Jupyter notebook after installing packages
3. Install missing library: `pip install [library_name]`
4. Check if you're in the right environment: `pip list`

#### Issue: "No module named 'pandas'" 
**Solution**: Your virtual environment might not be activated in Jupyter
```bash
# Install ipykernel in your venv
pip install ipykernel

# Add your venv as a Jupyter kernel
python -m ipykernel install --user --name=data_analytics_env

# Then select this kernel in Jupyter: Kernel → Change kernel → data_analytics_env
```

### Data and File Issues

#### Issue: "File not found"
**Solutions**:
1. Check file path and ensure CSV is in same directory as notebook
2. Use absolute path: `/full/path/to/your/file.csv`
3. Check file name spelling (case sensitive on Mac/Linux)

#### Issue: "KeyError in DataFrame"
**Solution**: Check column names with `df.columns` - they might have spaces or different names

#### Issue: Large numbers hard to read
**Solution**: Use the format_currency() helper function provided in the notebook

### Jupyter Notebook Issues

#### Issue: Jupyter won't start
**Solutions**:
1. Make sure virtual environment is activated
2. Try: `jupyter notebook --no-browser`
3. Check if port 8888 is busy: `jupyter notebook --port=8889`

#### Issue: Kernel keeps dying
**Solutions**:
1. Restart kernel: Kernel → Restart
2. Check for infinite loops in your code
3. Reduce data size if working with large datasets

#### Issue: Plots not showing
**Solutions**:
1. Make sure you have `%matplotlib inline` in first cell
2. Always end plot cells with `plt.show()`
3. Try: `%matplotlib notebook` for interactive plots

### Getting Help

If you're still stuck:

1. **Check the error message carefully** - it usually tells you what's wrong
2. **Google the exact error message** - someone probably had the same issue
3. **Ask a classmate or instructor** during the workshop
4. **Check package versions**: `pip list` to see what's installed

### Quick Fix Commands

```bash
# Reset everything if nothing works:
deactivate                           # Exit current venv
rm -rf data_analytics_env           # Delete venv (Mac/Linux)
# rmdir /s data_analytics_env       # Delete venv (Windows)
python -m venv data_analytics_env   # Create new venv
source data_analytics_env/bin/activate  # Activate (Mac/Linux)
# data_analytics_env\Scripts\activate   # Activate (Windows)
pip install -r requirements.txt     # Reinstall packages
```

---

## 🏆 Bonus Challenges

If you finish early, try these advanced exercises:

### Challenge 1: Trend Analysis
Find month-over-month changes if multiple periods exist

### Challenge 2: Risk Assessment
Calculate and visualize all provisions and risk indicators

### Challenge 3: Comparative Ratios
Research and calculate additional financial ratios (debt-to-equity, working capital, etc.)

### Challenge 4: Interactive Dashboard
Use Plotly to create interactive visualizations

---

## 📚 Additional Resources

- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Gallery](https://matplotlib.org/stable/gallery/index.html)
- [Financial Ratios Explained](https://www.investopedia.com/financial-ratios-4689817)
- [Python for Finance](https://www.datacamp.com/courses/introduction-to-python-for-finance)

---

## 📝 Submission

### What to Submit
1. Your completed Jupyter notebook (`.ipynb` file)
2. HTML export of your notebook (`File → Download as → HTML`)

### Naming Convention
`YourName_FinancialAnalysis_Workshop.ipynb`

### Due Date
End of class or as specified by instructor

---

## ❓ Need Help?

- **During class**: Raise your hand or ask the instructor
- **After class**: Post in the course forum
- **Email**: [instructor email]

---

## 🎉 Congratulations!

By completing this workshop, you've taken your first step into data analytics! You've learned to:
- Transform raw data into insights
- Use Python for financial analysis
- Create professional visualizations
- Generate business recommendations

**Next Class Preview**: Deep dive into pandas and advanced data manipulation

---

*Workshop created for Data Analytics Course - Class 1*  
*Instructor: Julian Eduardo Garzon Giraldo, MsC*