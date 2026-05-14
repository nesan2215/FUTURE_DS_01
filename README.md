# 📊 Business Sales Performance Analytics
### Future Interns — Data Science & Analytics Internship | Task 1 | FUTURE_DS_01

![Python](https://img.shields.io/badge/Python-3.x-blue?style=flat&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-green?style=flat&logo=pandas)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange?style=flat)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-9cf?style=flat)
![Status](https://img.shields.io/badge/Status-Completed-brightgreen?style=flat)

---

## 🔍 Project Overview

This project analyzes **12 months of real e-commerce transaction data** from a UK-based online retailer to uncover revenue trends, top-performing products, category performance, and regional sales patterns.

The goal was to think and deliver like a real data analyst — not just build charts, but answer actual business questions and provide actionable recommendations.

---

## ❓ Business Questions Answered

- Which products generate the most revenue?
- How does revenue change over time — and why?
- Which categories and regions are most profitable?
- Where should the business focus to grow faster?
- Which international markets have the highest potential?

---

## 📁 Dataset

| Detail | Info |
|--------|------|
| **Name** | Online Retail Dataset |
| **Source** | [Kaggle — UCI Online Retail](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset) |
| **Period** | December 2010 – December 2011 |
| **Raw Records** | 541,909 transactions |
| **Clean Records** | 397,924 transactions |
| **Countries** | 37 |

### Dataset Columns

| Column | Description |
|--------|-------------|
| `InvoiceNo` | Unique transaction ID |
| `StockCode` | Product code |
| `Description` | Product name |
| `Quantity` | Units purchased |
| `InvoiceDate` | Date & time of transaction |
| `UnitPrice` | Price per unit (GBP) |
| `CustomerID` | Unique customer ID |
| `Country` | Customer's country |

---

## 🛠️ Tools & Libraries

| Tool | Purpose |
|------|---------|
| `Python 3.x` | Core programming language |
| `Pandas` | Data loading, cleaning, aggregation |
| `NumPy` | Numerical operations |
| `Matplotlib` | Plotting and figure layout |
| `Seaborn` | Statistical visualizations |
| `ReportLab` | PDF report generation |

---

## 🧹 Data Cleaning Steps

- Dropped rows with missing `CustomerID` or `Description`
- Removed cancelled orders (InvoiceNo starting with `C`)
- Filtered out rows where `Quantity <= 0` or `UnitPrice <= 0`
- Converted `InvoiceDate` to datetime format
- Engineered new columns: `Revenue`, `Year`, `Month`, `YearMonth`, `DayOfWeek`

---

## 📊 Key Performance Indicators

| KPI | Value |
|-----|-------|
| 💰 Total Revenue | £9,747,748 |
| 🧾 Total Orders | 22,190 |
| 👥 Unique Customers | 4,372 |
| 📦 Units Sold | 5,176,450 |
| 🛒 Avg Order Value | £439.28 |
| 🌍 Countries Served | 37 |

---

## 📈 Key Insights

1. **Revenue Concentration Risk** — 84% of revenue comes from the UK alone, creating a single-market dependency risk.
2. **November Peak** — November 2011 hit £1.46M (36% above October) driven by pre-Christmas demand.
3. **High-Price vs High-Volume Gap** — DOTCOM POSTAGE earns £97/unit while PAPER CRAFT earns just £1/unit across 80K+ units.
4. **International High-Value Markets** — Netherlands AOV is £2,904 and Australia is £1,652 — both are likely B2B wholesale buyers who are under-served.
5. **Mid-Week Buying Pattern** — Thursday and Wednesday drive 38% of weekly revenue — pointing to bulk B2B ordering behaviour.
6. **Post-Holiday Dip** — January sees a predictable -25% MoM drop — a recoverable gap with the right campaigns.

---

## ✅ Actionable Recommendations

- Pre-stock top 5 revenue products by September to capture the Oct–Nov demand surge
- Assign account managers to Netherlands and Australia — high-AOV B2B markets
- Run a post-Christmas campaign in January to reduce the predictable 25% revenue dip
- Reprice high-volume/low-revenue products — a £0.50 increase on 80K units = £40K extra revenue
- Target business customers with bulk-buy offers on Tuesday–Thursday
- Bundle Seasonal category products with Home Decor bestsellers to increase basket size
- Reduce UK revenue dependency from 84% to 70% through targeted EU/ANZ campaigns

---

## 📂 Repository Structure

```
FUTURE_DS_01/
├── FUTURE_DS_01_Sales_Analysis.py   # Main Python analysis script
├── FUTURE_DS_01_Report.pdf          # Full client-ready analysis report
├── FUTURE_DS_01_Dashboard.png       # Dashboard visualization
├── online_retail.csv                # Source dataset (download from Kaggle)
└── README.md                        # Project documentation
```

---

## ▶️ How to Run

1. **Clone the repository**
```bash
git clone https://github.com/nesan2215/FUTURE_DS_01.git
cd FUTURE_DS_01
```

2. **Install dependencies**
```bash
pip install pandas numpy matplotlib seaborn reportlab
```

3. **Download the dataset** from [Kaggle](https://www.kaggle.com/datasets/ulrikthygepedersen/online-retail-dataset) and place `online_retail.csv` in the project folder

4. **Run the analysis**
```bash
python FUTURE_DS_01_Sales_Analysis.py
```

---

## 📄 Report Preview

The full analysis report (`FUTURE_DS_01_Report.pdf`) includes:
- Executive Summary
- KPI Dashboard
- Revenue Trend Analysis with MoM Growth
- Top 10 Product Analysis (Revenue + Quantity + Bubble Chart)
- Regional Market Analysis with Priority Classification
- Key Insights & Actionable Recommendations

---

## 🏢 About This Internship

This project was completed as part of the **Future Interns Data Science & Analytics Internship Program**.

- 🌐 Website: [futureinterns.com](https://futureinterns.com)
- 💼 LinkedIn: [Future Interns](https://www.linkedin.com/company/future-interns/)
- 📧 Contact: contact@futureinterns.com

---

## 👤 Author

**Nesan K**
- 💼 LinkedIn: [linkedin.com/in/nesan-k-bb995632b](https://www.linkedin.com/in/nesan-k-bb995632b)
- 🐙 GitHub: [github.com/nesan2215](https://github.com/nesan2215)

---

*This project is part of the Future Interns Internship Program — Task 1 of the Data Science & Analytics track.*
