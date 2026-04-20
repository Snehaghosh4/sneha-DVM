import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.io as pio

# Force Plotly to open in browser
pio.renderers.default = "browser"

# -------------------- LOAD DATA --------------------
file_path = "C:/Users/lab.AUKOL/Downloads/company_dataset.csv"

try:
    df = pd.read_csv(file_path)
    print("Dataset loaded successfully!\n")
except Exception as e:
    print("Error loading file:", e)
    exit()

# Clean column names
df.columns = df.columns.str.strip()

print("Columns in dataset:", df.columns.tolist())
print("\nFirst 5 rows:\n", df.head())

# -------------------- HELPER FUNCTION --------------------
def check_columns(required_cols):
    missing = [col for col in required_cols if col not in df.columns]
    if missing:
        print(f"Missing columns: {missing} → Skipping this section\n")
        return False
    return True

# -------------------- EMPLOYEES PIE CHART --------------------
if check_columns(['Company', 'Employees']):
    emp_data = df.groupby('Company')['Employees'].sum().sort_values(ascending=False).head(10)

    if not emp_data.empty:
        print("\nTop Companies by Employees:\n", emp_data)

        plt.figure(figsize=(8, 8))
        plt.pie(emp_data, labels=emp_data.index, autopct='%1.1f%%')
        plt.title("Employees Distribution (Top 10 Companies)")
        plt.show()

# -------------------- REVIEWS FUNNEL --------------------
if check_columns(['Company', 'Reviews']):
    review_data = df.groupby('Company')['Reviews'].sum().sort_values(ascending=False).head(10)

    if not review_data.empty:
        print("\nTop Companies by Reviews:\n", review_data)

        fig = px.funnel(
            x=review_data.values,
            y=review_data.index,
            title="Company Reviews Funnel (Top 10)"
        )
        fig.show()

# -------------------- HEADQUARTERS INFO --------------------
if check_columns(['Company', 'Employees', 'Headquarters']):
    top_companies = df.groupby('Company')['Employees'].sum().sort_values(ascending=False).head(10).reset_index()
    hq_data = df[['Company', 'Headquarters']].drop_duplicates()

    result = pd.merge(top_companies, hq_data, on='Company', how='left')

    print("\nTop 10 Companies with Headquarters:\n")
    print(result)

# -------------------- RATING BAR CHART --------------------
if check_columns(['Company', 'Rating']):
    rating_data = df.groupby('Company')['Rating'].mean().sort_values(ascending=False).head(10)

    if not rating_data.empty:
        print("\nTop Companies by Rating:\n", rating_data)

        plt.figure(figsize=(10, 6))
        plt.bar(rating_data.index, rating_data.values)
        plt.xticks(rotation=45, ha='right')
        plt.ylabel("Average Rating")
        plt.title("Top 10 Companies by Rating")
        plt.tight_layout()
        plt.show()

# -------------------- YEAR-WISE GROWTH --------------------
if check_columns(['Year', 'Company', 'Employees']):
    year_data = df.groupby(['Year', 'Company'])['Employees'].sum().reset_index()

    top5 = df.groupby('Company')['Employees'].sum().sort_values(ascending=False).head(5).index
    year_data = year_data[year_data['Company'].isin(top5)]

    plt.figure(figsize=(10, 6))

    for company in top5:
        subset = year_data[year_data['Company'] == company]
        plt.plot(subset['Year'], subset['Employees'], marker='o', label=company)

    plt.xlabel("Year")
    plt.ylabel("Employees")
    plt.title("Company Growth Year-wise (Top 5)")
    plt.legend()
    plt.grid(True)
    plt.show()
else:
    print("\nYear-wise data not available. Skipping line chart.")

# -------------------- KEEP WINDOW OPEN --------------------
input("\nPress Enter to exit...")