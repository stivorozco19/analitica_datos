# 🎓 Data Analytics Workshop: Antioquia Higher Education Scholarships Analysis

## 📋 Workshop Overview
In this hands-on workshop, you'll analyze real data about scholarship and credit beneficiaries for higher education access programs in Antioquia, Colombia. You'll apply the pandas and numpy concepts learned in class to extract meaningful insights from this dataset.

## 📊 Dataset Information
- **File**: `Beneficiaros_de_becas_y_creditos_de_programas_de_acceso_a_la_educaci_n_superior_de_Antioquia_20250815.csv`
- **Records**: ~14,500 scholarship beneficiaries
- **Columns**: 17 variables including demographics, education info, and program details
- **Time Period**: 2016 onwards
- **Source**: Government open data portal

### 🗂️ Key Columns
1. **CONVOCATORIA** - Call/Year
2. **BENEFICIO OTORGADO** - Benefit granted (scholarship type)
3. **GÉNERO** - Gender
4. **SUBREGIÓN DE RESIDENCIA** - Residence subregion
5. **ESTRATO** - Socioeconomic stratum (1-6)
6. **UNIVERSIDAD** - University
7. **TIPO DE FORMACIÓN** - Education level (Technical, Technological, University)
8. **GRADUADO** - Graduated (SI/NO)

## 🎯 Learning Objectives
By completing this workshop, you will:
- Apply the "Big 3" exploratory analysis methods
- Practice data cleaning and type conversion
- Use pandas filtering and groupby operations
- Work with numpy arrays for calculations
- Extract actionable insights from real-world data

---

## 📝 Workshop Tasks

### **Part 1: Data Loading and Initial Exploration** 🔍

#### Task 1.1: Load the Dataset
Load the CSV file and display basic information about the dataset.

**What you need to do:**
- Import necessary libraries (pandas, numpy)
- Load the CSV file using pandas
- Display the dataset dimensions

**Expected Results:**
- Dataset should have 14,566 rows and 17 columns
- All data should load successfully

#### Task 1.2: Apply the "Big 3" Analysis
Use the three most important methods for data exploration.

**What you need to do:**
- Display the first 5 rows to understand data structure
- Get general information about the dataset (data types, null values)
- Generate descriptive statistics for numerical columns

**Expected Results:**
- You should see mixed data types (some object, some numerical)
- Birth dates are stored as text/object format
- Most columns have complete data with minimal null values

#### Task 1.3: Column Analysis
Explore the available columns and their content.

**What you need to do:**
- Print all column names with their positions
- Check unique values for key categorical columns (GÉNERO, TIPO DE FORMACIÓN, GRADUADO)
- Count unique universities and programs

**Expected Results:**
- 17 columns total covering demographics, education, and program info
- GÉNERO should have 2 unique values
- GRADUADO should have SI/NO values
- Multiple universities and programs

---

### **Part 2: Data Cleaning and Preparation** 🧹

#### Task 2.1: Data Type Conversion
Clean and convert data types for proper analysis.

**What you need to do:**
- Convert ESTRATO to numerical format (handle text like "ESTRATO 1" → 1)
- Convert CONVOCATORIA to integer
- Create a function to clean and convert these columns
- Handle any conversion errors with `pd.to_numeric(errors='coerce')`

**Expected Results:**
- ESTRATO should become integer type with values 1-6
- CONVOCATORIA should be integer (years)
- No errors during conversion

#### Task 2.2: Data Quality Assessment
Check for data quality issues and handle them.

**What you need to do:**
- Check for null values in each column
- Identify which columns have missing data
- Calculate percentage of missing data per column
- Verify ESTRATO values are within expected range (1-6)

**Expected Results:**
- Missing data report showing count and percentage
- ESTRATO values should only be 1-6
- Most columns should have < 5% missing data

---

### **Part 3: Basic Analysis with Pandas** 📊

#### Task 3.1: Series Operations
Work with individual columns as Series.

**What you need to do:**
- Extract the GÉNERO column as a Series
- Calculate value counts for gender distribution
- Do the same for GRADUADO status
- Calculate graduation rate as a percentage

**Expected Results:**
- Gender distribution showing counts for MASCULINO/FEMENINO
- Graduation status showing SI/NO counts
- Overall graduation rate as a percentage

#### Task 3.2: DataFrame Filtering
Apply filters to find specific subsets of data.

**What you need to do:**
- Filter students from ESTRATO 1 only
- Find all graduated students
- Filter female students who graduated
- Find students from specific universities

**Expected Results:**
- Multiple filtered DataFrames with different row counts
- Should be able to see how filters reduce the dataset
- Combinations of filters should work correctly

#### Task 3.3: Using loc and iloc
Practice precise data selection.

**What you need to do:**
- Use iloc to select first 10 rows and columns 0-5
- Use loc to select specific columns for graduated students
- Use loc with conditions to filter and select columns simultaneously
- Compare the difference between loc and iloc

**Expected Results:**
- Precise selection of data subsets
- Understanding of position vs label-based indexing

---

### **Part 4: NumPy Integration** 🔢

#### Task 4.1: Converting to NumPy Arrays
Work with NumPy for numerical operations.

**What you need to do:**
- Convert ESTRATO column to NumPy array
- Calculate mean, median, standard deviation using NumPy
- Compare speed of operations: pandas vs NumPy
- Use NumPy to count specific values

**Expected Results:**
- NumPy operations should be faster
- Statistical calculations should match pandas results
- Arrays should handle numerical operations efficiently

#### Task 4.2: Vectorized Operations
Apply NumPy's vectorization capabilities.

**What you need to do:**
- Create binary arrays (1/0) for graduated status
- Calculate graduation rate using NumPy mean
- Use NumPy to categorize ESTRATO into low (1-2), medium (3-4), high (5-6)
- Apply conditional operations with NumPy

**Expected Results:**
- Binary array with 1 for graduated, 0 for not graduated
- Efficient categorization without loops
- Fast conditional operations

---

### **Part 5: GroupBy and Aggregations** 🔬

#### Task 5.1: Single Variable GroupBy
Analyze data by individual categories.

**What you need to do:**
- Group by GÉNERO and calculate graduation rates
- Group by ESTRATO and count students
- Group by TIPO DE FORMACIÓN and analyze distribution
- Group by UNIVERSIDAD and find top 10 by student count

**Expected Results:**
- Graduation rates by gender (should show percentage differences)
- Student distribution across socioeconomic strata
- Clear differences between education types
- Ranking of universities by enrollment

#### Task 5.2: Multiple Aggregations
Apply multiple functions to grouped data.

**What you need to do:**
- Group by SUBREGIÓN and calculate count, graduation rate, and most common stratum
- Use `.agg()` with multiple functions
- Create summary statistics for each group
- Sort results by different metrics

**Expected Results:**
- Comprehensive summary table by subregion
- Multiple metrics calculated simultaneously
- Sorted rankings showing best/worst performing groups

#### Task 5.3: Multi-level GroupBy
Analyze combinations of variables.

**What you need to do:**
- Group by GÉNERO and TIPO DE FORMACIÓN together
- Calculate graduation rates for each combination
- Group by ESTRATO and GRADUADO to see patterns
- Create pivot-table-like summaries

**Expected Results:**
- Cross-tabulation showing graduation rates by gender and education type
- Clear patterns in socioeconomic factors
- Multi-dimensional insights

---

### **Part 6: Advanced Filtering and Analysis** 🎯

#### Task 6.1: Complex Conditions
Apply multiple conditions for detailed analysis.

**What you need to do:**
- Find female students from ESTRATO 1 or 2 who graduated
- Filter students from specific universities AND programs
- Use `isin()` for multiple value filtering
- Combine conditions with & (and) and | (or)

**Expected Results:**
- Precise filtered datasets meeting all conditions
- Ability to answer specific questions about subgroups
- Understanding of boolean logic in pandas

#### Task 6.2: Top and Bottom Analysis
Identify best and worst performing segments.

**What you need to do:**
- Find top 5 universities by graduation rate (minimum 50 students)
- Identify programs with lowest graduation rates
- Use `nlargest()` and `nsmallest()` methods
- Calculate and rank by custom metrics

**Expected Results:**
- Rankings of best performing institutions
- Identification of programs needing improvement
- Clear performance differences

---

### **Part 7: Insights and Conclusions** 💡

#### Task 7.1: Key Metrics Summary
Calculate and present key performance indicators.

**What you need to do:**
- Calculate overall graduation rate
- Find average students per year (CONVOCATORIA)
- Determine most common student profile
- Calculate gender gap in graduation rates

**Expected Results:**
- Overall graduation rate: [specific percentage]
- Annual enrollment trends
- Typical beneficiary characteristics
- Quantified gender differences

#### Task 7.2: Program Effectiveness Analysis
Evaluate program impact across different segments.

**What you need to do:**
- Compare graduation rates: ESTRATO 1-2 vs 3-4 vs 5-6
- Analyze which education type has best outcomes
- Identify regions with best/worst performance
- Find correlations between variables

**Expected Results:**
- Clear socioeconomic patterns
- Education type effectiveness ranking
- Regional performance differences
- Data-driven conclusions

#### Task 7.3: Export Results
Save your findings for reporting.

**What you need to do:**
- Create summary DataFrames with key findings
- Export top performing universities to CSV
- Save graduation rate analysis by different categories
- Document your methodology and findings

**Expected Results:**
- CSV files with analysis results
- Clean, well-formatted output tables
- Reproducible analysis

---

## 🎯 Success Criteria

### Minimum Requirements (Pass):
- [ ] Successfully load and explore the dataset
- [ ] Apply data cleaning techniques
- [ ] Perform basic groupby analysis
- [ ] Calculate graduation rates by different categories
- [ ] Identify key patterns in the data

### Advanced Level (Excellent):
- [ ] Handle all data quality issues properly
- [ ] Perform sophisticated multi-dimensional analysis
- [ ] Create comprehensive summary tables
- [ ] Generate actionable insights with specific numbers
- [ ] Apply NumPy for efficient calculations

## 💪 Challenge Questions

If you finish early, try these advanced challenges:

1. **🔢 Statistical Deep Dive**: Calculate standard deviation of graduation rates by university
2. **🎯 Precision Analysis**: Find the exact student profile with highest graduation probability
3. **📊 Trend Analysis**: Analyze how graduation rates changed over years
4. **🌍 Regional Patterns**: Find which subregion-stratum combination performs best
5. **💡 Insights Mining**: Identify 3 non-obvious patterns in the data

## 🚀 Getting Started Tips

1. **Start Simple**: Begin with basic exploration before complex analysis
2. **Clean Early**: Fix data types before doing calculations
3. **Check Results**: Verify your numbers make sense
4. **Use Vectorization**: Prefer NumPy/pandas operations over loops
5. **Document Findings**: Keep notes of interesting discoveries

## ⚠️ Common Pitfalls to Avoid

- Not converting ESTRATO to numeric before calculations
- Forgetting to handle missing values
- Using loops instead of vectorized operations
- Not checking data types with `info()`
- Forgetting to filter before calculating rates

---

**Good luck with your analysis! 🎉**

*Remember: The goal is not just to complete the tasks, but to understand the stories the data tells about educational opportunity and success in Antioquia.*