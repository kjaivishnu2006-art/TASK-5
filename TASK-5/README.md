# Data Analyst Internship Portfolio

Welcome to my **Data Analyst Internship Portfolio**! This repository consolidates a comprehensive 8-day internship project demonstrating end-to-end data analysis skills, from raw data handling to actionable business insights.

---

## 📊 Portfolio Overview

This internship focused on analyzing a **retail sales dataset spanning 2020–2024** containing **1,194 transactions from 802 unique customers** across multiple product categories. The project demonstrated a complete analytic workflow: data preparation, exploratory analysis, customer segmentation, and hypothesis testing.

### Key Outcomes:
- 📈 **Revenue Analyzed**: $6.18M with 26.05% profit margin  
- 👥 **Customer Segments**: 5 RFM-based customer tiers identified (Champions, Loyal Customers, At-Risk, etc.)
- 📉 **Critical Finding**: Repeat customer rate of 0.62% (vs. 30%+ industry benchmark) — **statistically significant retention issue identified**
- 🔬 **Validation**: Hypothesis testing confirmed low retention is not due to chance

---

## 🎯 Project Architecture

This portfolio is organized into **4 core analytical tasks**:

### **[TASK-1: Data Wrangling & Cleaning](./TASK-1/)**
**Objective**: Establish a clean, validated dataset foundation  
**Key Deliverables**:
- ✅ Removed 2 duplicate records
- ✅ Standardized date formats and text fields
- ✅ Validated 12 columns across 1,194 transactions
- ✅ Created data dictionary documenting all fields

**Key Files**:
- `Sales Dataset_Cleaned.csv` — Production-ready dataset
- `data_cleaning.py` — Python cleaning pipeline
- `Data dictionary.csv` — Column definitions and data types

**Technical Skills**: Data validation, Python pandas, CSV processing, data quality assurance

---

### **[TASK-2: Cohort & Retention Analysis](./TASK-2/)**
**Objective**: Understand customer lifecycle patterns and retention trends  
**Key Deliverables**:
- ✅ Built cohort retention table tracking 802 customers across 24 months
- ✅ Identified critical 4-month retention drop-off
- ✅ Segmented customers into 5 RFM-based tiers
- ✅ Generated KPI summary: cohort size, retention %, repeat purchase rate

**Key Findings**:
- **Repeat Customer Rate**: 0.62% (significantly below 30%+ benchmark)
- **Top Customer Concentration**: 16% of customers ("Champions") drive disproportionate revenue
- **Untapped Potential**: 35% of customers in "Potential Loyalists" segment under-monetized

**Key Files**:
- `Cohort_Retention.csv` — Month-by-month retention heatmap
- `KPI_Summary.csv` — Aggregated performance metrics
- `deep_dive_analysis.py` — Cohort analysis implementation

**Technical Skills**: Cohort analysis, RFM segmentation, Pandas pivot tables, data storytelling

---

### **[TASK-3: Deep-Dive Analysis & KPI Visualization](./TASK-3/)**
**Objective**: Create executive-ready insights and interactive visualizations  
**Key Deliverables**:
- ✅ Built interactive Jupyter notebooks for exploratory data analysis
- ✅ Created dynamic KPI dashboards with profitability trends
- ✅ Analyzed customer lifecycle metrics across geographic regions
- ✅ Generated Excel reports for business stakeholder review

**Key Analyses**:
- **Temporal Trends**: Revenue and profit patterns (2020–2024)
- **Geographic Distribution**: State-level and city-level performance
- **Product Performance**: Category-level profitability and volume analysis
- **Customer Metrics**: Average order value, lifetime value projections, churn signals

**Key Files**:
- `KPI_Analysis.ipynb` — Interactive KPI dashboard (Jupyter)
- `Deep-Dive Analysis.ipynb` — Comprehensive EDA and advanced visualizations
- `kpi_excel_export.py` — Export pipeline for business stakeholders

**Technical Skills**: Jupyter notebooks, data visualization, Python (NumPy, Pandas, Matplotlib), business analytics, Excel integration

---

### **[TASK-4: Hypothesis Testing & Statistical Validation](./TASK-4/)**
**Objective**: Validate key business insights with statistical rigor  
**Key Deliverables**:
- ✅ Conducted hypothesis testing on retention metrics
- ✅ Calculated statistical significance and confidence intervals
- ✅ Validated that low retention is **not due to random chance**
- ✅ Generated comprehensive testing summary with actionable recommendations

**Hypothesis Tested**:
- **H₀ (Null)**: Repeat customer rate = Industry benchmark (30%+)
- **H₁ (Alternative)**: Repeat customer rate ≠ Industry benchmark
- **Result**: **Reject H₀** — Low retention is statistically significant (p < 0.05)

**Key Files**:
- `HYPOTHESIS_TESTING SUMMARY.md` — Full statistical analysis and recommendations

**Technical Skills**: Statistical hypothesis testing, p-value interpretation, confidence intervals, business recommendations

---

## 📈 Key Insights Summary

| Metric | Value | Insight |
|--------|-------|---------|
| **Total Revenue** | $6.18M | Solid revenue base |
| **Profit Margin** | 26.05% | Healthy profitability |
| **Unique Customers** | 802 | Small customer base |
| **Repeat Rate** | 0.62% | ⚠️ **Critical Issue** |
| **Industry Benchmark** | 30%+ | Significant gap |
| **Top 16% Customers** | Champions | Concentrated revenue dependence |
| **Retention Drop-Off** | Month 4 | Key intervention point |

---

## 💡 Recommendations

Based on the complete analysis:

1. **Immediate**: Design targeted retention programs for "Potential Loyalists" segment (35% of base)
2. **Short-term**: Implement win-back campaigns for "At-Risk" customers (inactive 6+ months)
3. **Medium-term**: Build loyalty program to reduce churn and increase repeat purchases
4. **Long-term**: Expand customer acquisition with retention infrastructure in place

---

## 🛠️ Technical Stack

- **Languages**: Python 3.x, SQL concepts
- **Libraries**: Pandas, NumPy, Matplotlib, Seaborn, SciPy
- **Notebooks**: Jupyter Lab
- **Data Tools**: Excel, CSV processing
- **Analysis Methods**: RFM segmentation, cohort analysis, hypothesis testing, data visualization
- **Version Control**: Git/GitHub

---

## 📁 Repository Structure

```
[YourName]-DataAnalyst-Internship-Portfolio/
├── README.md (← You are here)
├── TASK-1/
│   ├── Sales Dataset.csv
│   ├── Sales Dataset_Cleaned.csv
│   ├── Data dictionary.csv
│   └── data_cleaning.py
├── TASK-2/
│   ├── Cohort_Retention.csv
│   ├── KPI_Summary.csv
│   └── deep_dive_analysis.py
├── TASK-3/
│   ├── KPI_Analysis.ipynb
│   ├── Deep-Dive Analysis.ipynb
│   ├── kpi_excel_export.py
│   └── Sales Dataset.csv
├── TASK-4/
│   └── HYPOTHESIS_TESTING SUMMARY.md
├── TASK-5/
│   ├── README.md (Portfolio Master)
│   ├── LEARNING_SUMMARY.md
│   ├── PRESENTATION_SUMMARY.md
│   └── docs/
│       └── LINKEDIN_REFLECTION.md
└── .gitignore
```

---

## 🎓 Key Learnings & Technical Skills Demonstrated

### Data Engineering
- ✅ Data cleaning and validation pipelines
- ✅ Handling missing values and duplicates
- ✅ Data transformation and normalization
- ✅ CSV and Excel file processing

### Analysis & Insights
- ✅ Exploratory Data Analysis (EDA)
- ✅ Cohort analysis and retention tracking
- ✅ RFM customer segmentation
- ✅ Trend analysis and forecasting foundations
- ✅ Geographic performance analysis

### Statistics & Business Impact
- ✅ Hypothesis testing and p-value interpretation
- ✅ Confidence intervals and statistical significance
- ✅ Business metrics (KPIs, ROI, retention rates)
- ✅ Data-driven recommendations

### Tools & Programming
- ✅ Python programming (Pandas, NumPy, SciPy)
- ✅ Jupyter Notebook development
- ✅ Data visualization (Matplotlib, Seaborn)
- ✅ SQL concepts and relational databases
- ✅ Excel and CSV workflows

### Soft Skills
- ✅ Business communication and storytelling
- ✅ Stakeholder-ready documentation
- ✅ Complex problem decomposition
- ✅ Attention to detail and data quality

---

## 📞 Contact & Links

- **LinkedIn**: [Your LinkedIn Profile](https://linkedin.com/in/yourprofile)
- **GitHub**: [Your GitHub Profile](https://github.com/yourprofile)
- **Email**: your.email@example.com

---

## 📝 How to Use This Portfolio

1. **For Recruiters**: Start with this README for a 2-minute overview, then dive into individual TASK folders
2. **For Interviewers**: Review the Learning Summary and Presentation Summary documents
3. **For Technical Review**: Examine Python scripts and Jupyter notebooks for code quality
4. **For Data Review**: Check cleaned datasets and analysis outputs in each TASK folder

---

## 📄 License

This portfolio contains original analysis and code. Feel free to reference the methodology, but please credit the work appropriately.

---

**Last Updated**: March 2026  
**Portfolio Status**: Complete ✅  
**Timeline**: 8-Day Internship Project
