import pandas as pd
import numpy as np

# Load data
df = pd.read_csv('Sales Dataset.csv', parse_dates=['Order Date'])

# --- 1. KPI Calculations ---
# Total Sales
kpi_total_sales = df['Amount'].sum()
# Total Profit
kpi_total_profit = df['Profit'].sum()
# Average Order Value (AOV)
kpi_aov = df.groupby('Order ID')['Amount'].sum().mean()
# Order Quantity per Transaction
kpi_avg_qty = df.groupby('Order ID')['Quantity'].sum().mean()
# Customer Retention Rate (Cohort-based)
df['Year-Month'] = pd.to_datetime(df['Year-Month'], format='%Y-%m')
df['FirstPurchaseMonth'] = df.groupby('CustomerName')['Order Date'].transform('min').dt.to_period('M')
df['CohortMonth'] = df['FirstPurchaseMonth']
df['OrderMonth'] = df['Order Date'].dt.to_period('M')
df['CohortIndex'] = (df['OrderMonth'] - df['CohortMonth']).apply(lambda x: x.n)
cohort_data = df.groupby(['CohortMonth', 'CohortIndex'])['CustomerName'].nunique().reset_index()
cohort_pivot = cohort_data.pivot(index='CohortMonth', columns='CohortIndex', values='CustomerName')
cohort_size = cohort_pivot.iloc[:,0]
retention = cohort_pivot.divide(cohort_size, axis=0)

# Save KPIs
kpi_summary = pd.DataFrame({
    'KPI': ['Total Sales', 'Total Profit', 'Average Order Value', 'Avg Order Quantity'],
    'Value': [kpi_total_sales, kpi_total_profit, kpi_aov, kpi_avg_qty]
})
kpi_summary.to_csv('KPI_Summary.csv', index=False)

# Save Cohort Retention Table
retention.to_csv('Cohort_Retention.csv')

# Save Cleaned Data for Dashboard
cleaned_cols = ['Order ID','Amount','Profit','Quantity','Category','Sub-Category','PaymentMode','Order Date','CustomerName','State','City','Year-Month']
df[cleaned_cols].to_csv('Sales_Cleaned.csv', index=False)

print('KPI Summary:')
print(kpi_summary)
print('\nCohort Retention Table (first 5 rows):')
print(retention.head())
print('\nData prepared for dashboarding.')
