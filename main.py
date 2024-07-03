import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset
df = pd.read_csv('data.csv')

# Step 2: Data cleaning and preparation
# Check for missing values
print(df.isnull().sum())

# Convert data types if needed
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Sales'] = df['Quantity Ordered'] * df['Price Each']

# Step 3: Data analysis

# Monthly sales analysis
monthly_sales = df.groupby('Month')['Sales'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.barplot(x='Month', y='Sales', data=monthly_sales, palette='viridis', hue='Month', dodge=False)
plt.legend([],[], frameon=False)  # Remove legend
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.xticks(rotation=45)
plt.show()

# Hourly sales analysis
df['Hour'] = df['Order Date'].dt.hour
hourly_sales = df.groupby('Hour')['Sales'].sum().reset_index()
plt.figure(figsize=(10, 6))
sns.lineplot(x='Hour', y='Sales', data=hourly_sales, marker='o', linestyle='-', color='b')
plt.title('Hourly Sales')
plt.xlabel('Hour')
plt.ylabel('Sales ($)')
plt.xticks(range(0, 25, 2))
plt.grid(True)
plt.show()

# Top products sold
top_products = df['Product'].value_counts().head(10).reset_index()
top_products.columns = ['Product', 'Orders']
plt.figure(figsize=(10, 6))
sns.barplot(x='Product', y='Orders', data=top_products, palette='coolwarm', hue='Product', dodge=False)
plt.legend([],[], frameon=False)  # Remove legend
plt.title('Top 10 Products Sold')
plt.xlabel('Product')
plt.ylabel('Number of Orders')
plt.xticks(rotation=90)
plt.show()

# Step 4: Insights and conclusion

# Monthly sales insights
max_month = monthly_sales.loc[monthly_sales['Sales'].idxmax(), 'Month']
max_sales = monthly_sales['Sales'].max()
min_month = monthly_sales.loc[monthly_sales['Sales'].idxmin(), 'Month']
min_sales = monthly_sales['Sales'].min()
print(f"Highest sales occur in {max_month} with ${max_sales:,.0f}")
print(f"Lowest sales occur in {min_month} with ${min_sales:,.0f}")

# Hourly sales insights
peak_hour = hourly_sales.loc[hourly_sales['Sales'].idxmax(), 'Hour']
peak_sales = hourly_sales['Sales'].max()
print(f"The peak sales hour is around {peak_hour}:00 with ${peak_sales:,.0f} in sales")

# Top products insights
top_product = top_products.loc[top_products['Orders'].idxmax(), 'Product']
top_product_orders = top_products['Orders'].max()
print(f"The top selling product is '{top_product}' with {top_product_orders} orders")

# Additional insights and recommendations based on findings
print("\nAdditional Insights:")
print("- Consider focusing marketing efforts around peak sales hours.")
print("- Explore opportunities to promote and bundle the top selling products.")

# Conclusion
print("\nConclusion:")
print(f"- The analysis reveals strong seasonal trends, with {max_month} exhibiting the highest sales.")
print(f"- Certain hours of the day see significantly higher sales volumes, suggesting potential for targeted promotions.")
print(f"- Product '{top_product}' consistently performs well and should be a focal point for inventory management and marketing strategies.")

# Example actions based on insights
print("\nRecommendations:")
print("- Implement targeted marketing campaigns during peak sales periods and for top-selling products.")
print("- Optimize inventory levels for high-demand products based on monthly and hourly trends.")