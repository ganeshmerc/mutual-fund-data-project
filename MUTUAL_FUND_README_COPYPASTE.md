# 💰 Mutual Fund Data Analysis

Comprehensive exploratory data analysis (EDA) on mutual fund performance, comparing returns, risk metrics, and portfolio composition.

## 📊 Project Overview
An in-depth analysis of mutual fund data to help investors understand performance patterns, risk profiles, and investment potential.

## 🎯 Analysis Objectives
- Compare fund performance across different categories
- Analyze risk-return relationships
- Identify top-performing funds
- Understand portfolio composition trends

## 📈 Key Findings
- Identified top 10 funds by 5-year returns
- Risk-return scatter plot analysis
- Correlation analysis between fund categories
- Performance attribution analysis

## 🛠️ Tools & Libraries
- **Python 3.x**
- **Pandas** - Data manipulation & analysis
- **NumPy** - Numerical computations
- **Matplotlib & Seaborn** - Data visualization
- **Jupyter Notebook** - Interactive analysis

## 📁 Project Structure
```
├── data/
│   ├── mutual_fund_data.csv
│   └── fund_categories.xlsx
├── notebooks/
│   ├── 01_data_loading_cleaning.ipynb
│   ├── 02_exploratory_analysis.ipynb
│   └── 03_performance_analysis.ipynb
├── visualizations/
│   ├── returns_distribution.png
│   ├── risk_return_scatter.png
│   └── correlation_heatmap.png
└── README.md
```

## 📊 Analysis Sections
1. **Data Loading & Cleaning** - Handle missing values, outliers
2. **Descriptive Statistics** - Summary metrics for all funds
3. **Performance Analysis** - Returns, Sharpe ratios, max drawdown
4. **Risk Assessment** - Volatility, beta, risk metrics
5. **Visualization** - Charts and plots for insights

## 🔍 Key Visualizations
- Performance distribution plot
- Risk vs. Return scatter
- Correlation heatmap
- Rolling returns analysis
- Drawdown analysis

## 💡 Insights
- Equity funds show higher returns but with increased volatility
- Balanced funds offer moderate risk-return profile
- Debt funds provide stable returns with lower risk
- Diversification reduces portfolio risk

## 🚀 How to Use
1. Clone the repository
2. Install requirements: `pip install -r requirements.txt`
3. Run Jupyter: `jupyter notebook`
4. Open analysis notebooks in order

## 📚 Requirements
```
pandas>=1.3.0
numpy>=1.21.0
matplotlib>=3.4.0
seaborn>=0.11.0
jupyter>=1.0.0
```

## 🔄 Future Enhancements
- [ ] Predictive modeling for returns
- [ ] Monte Carlo simulation
- [ ] Portfolio optimization
- [ ] Risk factor analysis

---

*Last Updated: August 2026*
