import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
import seaborn as sns
import warnings
warnings.filterwarnings("ignore")

df = pd.read_csv("online_retail.csv", encoding="ISO-8859-1")

print(df.shape)
print(df.head())
print(df.isnull().sum())
print(df.dtypes)

df.dropna(subset=["CustomerID", "Description"], inplace=True)
df = df[~df["InvoiceNo"].astype(str).str.startswith("C")]
df = df[(df["Quantity"] > 0) & (df["UnitPrice"] > 0)]
df["InvoiceDate"] = pd.to_datetime(df["InvoiceDate"])
df["Revenue"] = df["Quantity"] * df["UnitPrice"]
df["Year"] = df["InvoiceDate"].dt.year
df["Month"] = df["InvoiceDate"].dt.month
df["MonthName"] = df["InvoiceDate"].dt.strftime("%b")
df["YearMonth"] = df["InvoiceDate"].dt.to_period("M")
df["DayOfWeek"] = df["InvoiceDate"].dt.day_name()

print(df.shape)
print(df.describe())

total_revenue = df["Revenue"].sum()
total_orders = df["InvoiceNo"].nunique()
total_customers = df["CustomerID"].nunique()
avg_order_value = total_revenue / total_orders
total_units = df["Quantity"].sum()

print(f"Total Revenue: £{total_revenue:,.2f}")
print(f"Total Orders: {total_orders}")
print(f"Total Customers: {total_customers}")
print(f"Avg Order Value: £{avg_order_value:,.2f}")
print(f"Units Sold: {total_units}")

monthly_revenue = df.groupby("YearMonth")["Revenue"].sum().reset_index().sort_values("YearMonth")
monthly_revenue["YearMonth"] = monthly_revenue["YearMonth"].astype(str)

top_products_revenue = df.groupby("Description")["Revenue"].sum().sort_values(ascending=False).head(10).reset_index()
top_products_qty = df.groupby("Description")["Quantity"].sum().sort_values(ascending=False).head(10).reset_index()

regional = df.groupby("Country").agg(Revenue=("Revenue","sum"), Orders=("InvoiceNo","nunique")).sort_values("Revenue", ascending=False).head(10).reset_index()

day_order = ["Monday","Tuesday","Wednesday","Thursday","Friday","Sunday"]
day_revenue = df.groupby("DayOfWeek")["Revenue"].sum().reindex(day_order).reset_index()

print(top_products_revenue)
print(regional)

sns.set_style("darkgrid")
plt.rcParams.update({
    "figure.facecolor": "#0f0f1a",
    "axes.facecolor": "#1a1a2e",
    "axes.labelcolor": "white",
    "xtick.color": "white",
    "ytick.color": "white",
    "text.color": "white",
    "grid.color": "#2e2e4e",
})

fig = plt.figure(figsize=(20, 24))
fig.patch.set_facecolor("#0f0f1a")
fig.suptitle("Business Sales Performance Dashboard", fontsize=22, fontweight="bold", color="white", y=0.98)

ax1 = fig.add_subplot(4, 2, (1, 2))
ax1.plot(monthly_revenue["YearMonth"], monthly_revenue["Revenue"], color="#00d4ff", linewidth=2.5, marker="o", markersize=5)
ax1.fill_between(monthly_revenue["YearMonth"], monthly_revenue["Revenue"], alpha=0.2, color="#00d4ff")
ax1.set_title("Monthly Revenue Trend")
ax1.set_xlabel("Month")
ax1.set_ylabel("Revenue (£)")
ax1.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"£{x:,.0f}"))
ax1.tick_params(axis="x", rotation=45)

ax2 = fig.add_subplot(4, 2, 3)
colors1 = sns.color_palette("coolwarm", 10)
bars = ax2.barh(top_products_revenue["Description"].str[:30], top_products_revenue["Revenue"], color=colors1)
ax2.set_title("Top 10 Products by Revenue")
ax2.set_xlabel("Revenue (£)")
ax2.invert_yaxis()
for bar in bars:
    ax2.text(bar.get_width() + 200, bar.get_y() + bar.get_height()/2, f"£{bar.get_width():,.0f}", va="center", fontsize=7, color="white")

ax3 = fig.add_subplot(4, 2, 4)
colors2 = sns.color_palette("viridis", 10)
bars2 = ax3.barh(top_products_qty["Description"].str[:30], top_products_qty["Quantity"], color=colors2)
ax3.set_title("Top 10 Products by Quantity")
ax3.set_xlabel("Quantity")
ax3.invert_yaxis()
for bar in bars2:
    ax3.text(bar.get_width() + 100, bar.get_y() + bar.get_height()/2, f"{bar.get_width():,}", va="center", fontsize=7, color="white")

ax4 = fig.add_subplot(4, 2, 5)
sns.barplot(data=regional, x="Revenue", y="Country", palette="magma", ax=ax4)
ax4.set_title("Top 10 Countries by Revenue")
ax4.set_xlabel("Revenue (£)")
ax4.xaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"£{x/1e3:.0f}K"))

ax5 = fig.add_subplot(4, 2, 6)
sns.barplot(data=regional, x="Orders", y="Country", palette="crest", ax=ax5)
ax5.set_title("Top 10 Countries by Orders")
ax5.set_xlabel("Number of Orders")

ax6 = fig.add_subplot(4, 2, 7)
sns.barplot(data=day_revenue, x="DayOfWeek", y="Revenue", palette="flare", ax=ax6)
ax6.set_title("Revenue by Day of Week")
ax6.set_xlabel("Day")
ax6.set_ylabel("Revenue (£)")
ax6.yaxis.set_major_formatter(mticker.FuncFormatter(lambda x, _: f"£{x/1e3:.0f}K"))
ax6.tick_params(axis="x", rotation=30)

ax7 = fig.add_subplot(4, 2, 8)
ax7.axis("off")
kpi_text = (
    f"KPI SUMMARY\n\n"
    f"Total Revenue     : £{total_revenue:,.2f}\n\n"
    f"Total Orders       : {total_orders:,}\n\n"
    f"Total Customers  : {total_customers:,}\n\n"
    f"Units Sold          : {total_units:,}\n\n"
    f"Avg Order Value  : £{avg_order_value:,.2f}\n\n"
    f"Countries Served : {df['Country'].nunique()}"
)
ax7.text(0.1, 0.5, kpi_text, transform=ax7.transAxes, fontsize=11,
         verticalalignment="center", color="white",
         bbox=dict(facecolor="#1a1a2e", edgecolor="#00d4ff", boxstyle="round,pad=1", linewidth=2))

plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.savefig("FUTURE_DS_01_Dashboard.png", dpi=150, bbox_inches="tight", facecolor="#0f0f1a")
plt.show()

top_country = regional.iloc[0]["Country"]
top_product = top_products_revenue.iloc[0]["Description"]
peak_month = monthly_revenue.loc[monthly_revenue["Revenue"].idxmax(), "YearMonth"]

print(f"Top Country: {top_country}")
print(f"Best Product: {top_product}")
print(f"Peak Month: {peak_month}")
print("UK dominates sales - focus on expanding to other countries")
print("November peak suggests pre-Christmas demand - plan inventory early")
print("Top products should always be kept in stock")
print("Mid-week promotions can help boost revenue on slower days")
