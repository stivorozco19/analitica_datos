# 🚰 Water Consumption Analysis Workshop - Class 5

## Systematic EDA Applied to Real-World Data

**Author:** Julian Eduardo Garzon Giraldo, MsC  
**Date:** Week 5 - Practical Application  
**Dataset:** Colombian Water Consumption by Socioeconomic Strata (2015-2023)

---

## 🎯 Workshop Objectives

In this hands-on workshop, you will apply the systematic EDA methodology learned in class to a real-world dataset containing water consumption data from Colombian municipalities. Your goal is to uncover actionable insights about water consumption patterns across different socioeconomic strata.

### **Learning Goals:**
- Apply the 5-step univariate analysis framework to real data
- Identify distribution types and their business implications
- Conduct bivariate analysis between different variable types
- Perform multivariate analysis to uncover hidden patterns
- Generate data-driven recommendations for policy makers

---

## 📊 Dataset Overview

### **File:** `HISTORICO_CONSUMO_POR_ESTRATO_20250906.csv`

**Dataset Description:**  
Historical water consumption data from Empocaldas S.A E.S.P (Caldas Water Company) spanning from 2015 to 2023. Contains monthly consumption records across different municipalities and socioeconomic strata.

**Size:** 21,817 records  
**Time Period:** January 2015 - May 2023  
**Geographic Coverage:** Multiple municipalities in Caldas, Colombia

### **Variables:**
- **NIT:** Company tax identification number
- **RAZON SOCIAL:** Company name (Empocaldas)
- **AÑO:** Year (2015-2023)
- **MES:** Month (Spanish names)
- **MUNICIPIO:** Municipality name
- **ESTRATO:** Socioeconomic stratum (1-6, Industrial, Commercial, Public/Official)
- **No. SUSCRIPTORES ACUEDUCTO:** Number of water service subscribers
- **CONSUMO M3 ACUEDUCTO:** Total water consumption (cubic meters)
- **PROMEDIO CONSUMO ACUEDUCTO:** Average water consumption per subscriber
- **No. SUSCRIPTORES ALCANTARILLADO:** Number of sewerage service subscribers  
- **CONSUMO M3 ALCANTARILLADO:** Total sewerage consumption (cubic meters)
- **PROMEDIO CONSUMO ALCANTARILLADO:** Average sewerage consumption per subscriber

### **Socioeconomic Strata Context:**
- **Estrato 1-2:** Low socioeconomic level (subsidized)
- **Estrato 3-4:** Middle socioeconomic level
- **Estrato 5-6:** High socioeconomic level (surtax)
- **Commercial:** Business establishments
- **Industrial:** Industrial facilities
- **Public/Official:** Government institutions

---

## 🔍 Analysis Challenges & Questions

### **Phase 1: Univariate Analysis (25 minutes)**

Apply your 5-step framework to key variables:

#### **🎯 Primary Questions:**
1. **Water Consumption Distribution:**
   - What type of distribution does average water consumption follow?
   - Are there significant outliers? What might explain them?
   - How does consumption vary across the 8+ years?

2. **Subscriber Base Analysis:**
   - How is the number of subscribers distributed across strata?
   - Which strata have the most/least coverage?
   - Are there seasonal patterns in subscriber numbers?

3. **Geographic Distribution:**
   - Which municipalities have the highest consumption?
   - How many municipalities are covered in the dataset?
   - Are there municipalities with unusual consumption patterns?

#### **🛠️ Tasks:**
- [ ] Analyze distribution of `PROMEDIO CONSUMO ACUEDUCTO`
- [ ] Examine `No. SUSCRIPTORES ACUEDUCTO` by stratum
- [ ] Investigate temporal patterns in consumption
- [ ] Identify and investigate outliers
- [ ] Create visualizations for each analysis

---

### **Phase 2: Bivariate Analysis**

Explore relationships between variables:

#### **🎯 Key Relationships to Explore:**
1. **Socioeconomic Stratum vs. Consumption:**
   - Do higher strata consume more water per capita?
   - How does this relationship vary by municipality?
   - Are there strata with unexpected consumption patterns?

2. **Temporal Patterns:**
   - How does consumption vary by month/season?
   - Has consumption changed over the 8-year period?
   - Are there growth or decline trends by stratum?

3. **Service Coverage Analysis:**
   - What's the relationship between water and sewerage subscribers?
   - Do areas with more subscribers have different consumption patterns?
   - How does coverage correlate with average consumption?

#### **🛠️ Tasks:**
- [ ] Compare consumption across strata (boxplots/violin plots)
- [ ] Analyze temporal trends (time series)
- [ ] Calculate correlations between key variables
- [ ] Create geographic consumption maps (if possible)
- [ ] Investigate water vs. sewerage service relationships

---

### **Phase 3: Multivariate Analysis**

Uncover complex patterns and interactions:

#### **🎯 Advanced Questions:**
1. **Geographic-Economic Interactions:**
   - Does the stratum-consumption relationship vary by municipality?
   - Are there municipalities where low strata consume more than expected?
   - Can we identify geographic clusters of consumption patterns?

2. **Temporal-Economic Evolution:**
   - How has the consumption gap between strata evolved over time?
   - Which strata showed the most dramatic changes during COVID-19 (2020-2021)?
   - Are there seasonal effects that vary by socioeconomic level?

3. **Service Efficiency Analysis:**
   - Do municipalities with better sewerage coverage have different water consumption?
   - Can we identify underperforming or overperforming municipalities?
   - What factors predict high consumption efficiency?

#### **🛠️ Tasks:**
- [ ] Segment analysis by municipality + stratum combinations
- [ ] Time series analysis by stratum groups
- [ ] Correlation analysis within subgroups
- [ ] Identify Simpson's Paradox examples
- [ ] Create multidimensional visualizations

---

### **Phase 4: Insights & Recommendations (15 minutes)**

Generate actionable findings:

#### **🎯 Business Questions to Answer:**
1. **Policy Implications:**
   - Which strata should be targeted for water conservation programs?
   - Are subsidies properly allocated based on actual consumption patterns?
   - What municipalities need infrastructure investment?

2. **Operational Insights:**
   - Can we predict seasonal demand fluctuations?
   - Which areas show sustainable consumption growth?
   - Are there efficiency benchmarks we can establish?

3. **Social Impact:**
   - Do consumption patterns reflect expected socioeconomic differences?
   - Are there equity issues in water access or consumption?
   - How has water consumption resilience varied during the pandemic?

#### **🛠️ Deliverables:**
- [ ] 3-5 key insights with supporting evidence
- [ ] Data-driven recommendations for stakeholders
- [ ] Identification of areas requiring further investigation
- [ ] Summary of data quality issues discovered

---

## 💻 Technical Setup

### **Required Libraries:**
```python
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import warnings
warnings.filterwarnings('ignore')

# Optional for advanced analysis
import plotly.express as px  # Interactive plots
import folium  # Geographic visualization
```

### **Data Loading Template:**
```python
# Load the dataset
df = pd.read_csv('HISTORICO_CONSUMO_POR_ESTRATO_20250906.csv')

# Basic exploration
print(f"Dataset shape: {df.shape}")
print(f"Date range: {df['AÑO'].min()} - {df['AÑO'].max()}")
print(f"Municipalities: {df['MUNICIPIO'].nunique()}")
print(f"Strata types: {df['ESTRATO'].unique()}")

# Check for data quality issues
print(f"Missing values per column:")
print(df.isnull().sum())
```

---

## 📋 Expected Data Quality Issues

Be prepared to handle:

### **Common Issues:**
- **Mixed number formats:** Some numbers use commas as thousands separators
- **Missing values:** Empty strings and NaN values
- **Inconsistent formatting:** Spanish month names, mixed data types
- **Zero consumption records:** May indicate service interruptions or data collection issues
- **Outliers:** Unusual consumption spikes or drops

### **Cleaning Suggestions:**
```python
# Convert numeric columns with commas
numeric_cols = ['AÑO', 'No. SUSCRIPTORES ACUEDUCTO', 'CONSUMO M3 ACUEDUCTO', 
                'PROMEDIO CONSUMO ACUEDUCTO', 'No. SUSCRIPTORES ALCANTARILLADO', 
                'CONSUMO M3 ALCANTARILLADO', 'PROMEDIO CONSUMO ALCANTARILLADO']

for col in numeric_cols:
    df[col] = pd.to_numeric(df[col].astype(str).str.replace(',', ''), errors='coerce')

# Handle month names (Spanish to English or numeric)
month_mapping = {
    'ENERO': 1, 'FEBRERO': 2, 'MARZO': 3, 'ABRIL': 4,
    'MAYO': 5, 'JUNIO': 6, 'JULIO': 7, 'AGOSTO': 8,
    'SEPTIEMBRE': 9, 'OCTUBRE': 10, 'NOVIEMBRE': 11, 'DICIEMBRE': 12
}
df['MES_NUM'] = df['MES'].map(month_mapping)
```

---

## 🏆 Success Criteria

Your analysis will be successful if you:

### **Technical Execution:**
- [ ] Apply the systematic EDA methodology correctly
- [ ] Handle data quality issues appropriately  
- [ ] Use appropriate visualization techniques for each variable type
- [ ] Conduct statistical analysis with proper interpretation

### **Business Impact:**
- [ ] Generate insights relevant to water utility management
- [ ] Identify patterns that could inform policy decisions
- [ ] Discover unexpected relationships or anomalies
- [ ] Provide evidence-based recommendations

### **Communication:**
- [ ] Create clear, interpretable visualizations
- [ ] Write concise, actionable insights
- [ ] Support conclusions with statistical evidence
- [ ] Identify limitations and areas for further investigation

---

## 🎓 Learning Assessment

This workshop tests your ability to:

1. **Apply methodology:** Use the 5-step univariate framework systematically
2. **Handle real data:** Deal with messy, imperfect datasets
3. **Think critically:** Question anomalies and investigate patterns
4. **Generate value:** Transform data analysis into business insights
5. **Communicate effectively:** Present findings clearly and convincingly

---

## 💡 Hints & Tips

### **Analysis Strategy:**
- Start with data quality assessment before diving into analysis
- Focus on the most impactful variables first
- Use segmentation to uncover hidden patterns
- Always validate unexpected findings
- Consider external factors (economic events, weather, policy changes)

### **Common Pitfalls to Avoid:**
- Don't ignore data quality issues
- Don't assume correlation implies causation
- Don't over-interpret small differences
- Don't forget to consider business context
- Don't present findings without supporting evidence

### **Advanced Techniques to Consider:**
- Time series decomposition for seasonal patterns
- Geographic clustering analysis
- Efficiency benchmarking between municipalities
- Predictive modeling for demand forecasting
- Equity analysis across socioeconomic strata

---

## 📈 Bonus Challenges

For advanced analysts:

1. **Efficiency Scoring:** Create a consumption efficiency index by municipality
2. **Predictive Analysis:** Build a model to predict monthly consumption
3. **Policy Impact:** Identify periods of significant consumption changes and correlate with known policy interventions
4. **Sustainability Analysis:** Assess which areas show sustainable consumption patterns
5. **Interactive Dashboard:** Create an interactive visualization showing consumption patterns over time and geography

---

## 🚀 Getting Started

1. **Download the dataset** from the workshop folder
2. **Set up your environment** with required libraries  
3. **Start with data exploration** - understand what you're working with
4. **Apply the systematic methodology** learned in class
5. **Document your findings** as you progress
6. **Prepare to present** your top 3 insights to the class

---

**⏰ Time Management:**
- **Data Loading & Cleaning:** 10 minutes
- **Univariate Analysis:** 25 minutes  
- **Bivariate Analysis:** 25 minutes
- **Multivariate Analysis:** 25 minutes
- **Insights & Recommendations:** 15 minutes

---

**🎯 Remember:** This is real data that could inform actual policy decisions. Your analysis could help improve water service delivery for thousands of Colombian families. Make it count!

---

**Good luck and happy analyzing! 💧📊**