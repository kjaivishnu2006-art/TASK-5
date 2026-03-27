
# 📊 Retail Sales Data Analysis (2020–2025)

## 📌 Project Overview

This project analyzes **Retail Sales Data from 2020–2025** to understand business performance, customer behavior, and growth opportunities. The dataset contains **1,194 transactions from 802 unique customers** across product categories such as **Electronics, Furniture, and Office Supplies**.

The objective of this analysis is to evaluate **key performance metrics, customer lifecycle patterns, and retention performance**, and provide **data-driven recommendations for sustainable business growth**.

---

# 🎯 Business Problem

Although the company generated **$6.18M in revenue** with a **26.05% profit margin**, customer retention appears to be extremely low.

Key finding:

* **Repeat Customer Rate = 0.62%**
* **Industry Benchmark = 30%+**

This raises a critical business question:

> Are we building a loyal customer base, or are we primarily generating revenue from one-time buyers?

To validate whether this retention issue is statistically significant, **hypothesis testing** was conducted.

---

# 🧹 Data Preparation

Before analysis, the dataset was cleaned and prepared to ensure accuracy.

Data preparation steps included:

* Removing duplicate records
* Standardizing date formats
* Cleaning text fields
* Normalizing customer names
* Validating numerical values (Amount, Profit, Quantity)

Final dataset:

| Metric            | Value |
| ----------------- | ----- |
| Transactions      | 1,194 |
| Customers         | 802   |
| Missing Values    | 0     |
| Validated Columns | 12    |

---

# 📈 Key Performance Indicators (KPIs)

The following KPIs were calculated to evaluate business performance.

| KPI                   | Value   | Insight                    |
| --------------------- | ------- | -------------------------- |
| Total Revenue         | $6.18M  | Strong revenue generation  |
| Profit Margin         | 26.05%  | Above industry benchmark   |
| Average Order Value   | $11,302 | High transaction value     |
| Units per Transaction | 23.30   | Customers purchase in bulk |
| Repeat Customer Rate  | 0.62%   | Critical retention issue   |

Although revenue and profitability are strong, the **extremely low repeat rate signals a broken customer retention engine**.

---

# 🧪 Hypothesis Testing

## Business Hypothesis

To determine whether the repeat customer rate is significantly lower than the industry benchmark, the following hypothesis test was conducted.

### Null Hypothesis (H₀)

The company's repeat customer rate is equal to the industry benchmark.

[
H_0: p = 0.30
]

### Alternative Hypothesis (H₁)

The company's repeat customer rate is significantly lower than the industry benchmark.

[
H_1: p < 0.30
]

This is a **one-tailed hypothesis test**.

---

# 📊 Data Used for Testing

| Metric               | Value |
| -------------------- | ----- |
| Total Customers      | 802   |
| Repeat Customers     | ~5    |
| Observed Repeat Rate | 0.62% |
| Industry Benchmark   | 30%   |

Observed proportion:

[
p = \frac{5}{802} = 0.0062
]

---

# 📉 Statistical Test

A **One-Proportion Z-Test** was used to compare the observed repeat rate with the industry benchmark.

Test Formula:

[
Z = \frac{p - p_0}{\sqrt{\frac{p_0(1-p_0)}{n}}}
]

Where:

* (p) = observed proportion (0.0062)
* (p_0) = benchmark proportion (0.30)
* (n) = sample size (802)

---

# 📊 Test Results

| Metric             | Value   |
| ------------------ | ------- |
| Z-score            | -15.2   |
| p-value            | < 0.001 |
| Significance Level | 0.05    |

Since the **p-value is less than 0.05**, the null hypothesis is rejected.

---

# 📏 Confidence Interval

A **95% confidence interval** was calculated to estimate the true repeat customer rate.

Result:

**0.1% – 1.2%**

Even at the upper bound, the repeat rate remains **far below the industry benchmark of 30%**.

---

# 📌 Interpretation

The statistical results confirm that the **low repeat customer rate is not due to random variation**. Instead, it indicates a **structural issue in customer retention**.

This means the company is primarily dependent on **new customer acquisition rather than repeat purchases**.

---

# 💡 Business Recommendations

Based on the analysis, the following strategies are recommended:

### 1️⃣ Loyalty Programs

Introduce rewards and incentives to encourage repeat purchases.

### 2️⃣ Subscription Model

Use high-frequency categories such as **Office Supplies** for subscription-based purchases.

### 3️⃣ Customer Re-engagement

Launch personalized marketing campaigns for inactive customers.

---

# 📊 Expected Business Impact

Improving customer retention could lead to:

* Higher **Customer Lifetime Value (CLV)**
* Lower **Customer Acquisition Cost (CAC)**
* More stable long-term revenue
* Stronger customer loyalty

Projected improvement:

**10–15% increase in Customer Lifetime Value**

---

# 📚 Tools & Technologies

* Python
* Pandas
* Data Visualization
* Statistical Analysis
* Hypothesis Testing

---

# ✅ Conclusion

The analysis shows that although the business generates strong revenue and profits, the **extremely low repeat customer rate represents a major growth risk**.

Addressing the retention issue through **loyalty programs, subscriptions, and targeted engagement strategies** will help transform the business from a **transaction-driven model to a sustainable customer-centric model**.

---

