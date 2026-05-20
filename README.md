# Insurance Charges Prediction 🏥💰

This project aims to predict the annual medical insurance charges of an individual based on their demographic and health characteristics (such as age, BMI, smoking habits, etc.) using Machine Learning.

## 📊 Project Overview
- **Dataset:** `insurance.csv` (1,338 rows, 7 columns)
- **Current Model:** Linear Regression (Baseline)
- **Model Evaluation:**
  - **$R^2$ Score:** ~80.4%
  - **Adjusted $R^2$ Score:** ~79.8%

## 🛠️ Tech Stack & Libraries
- **Language:** Python 3
- **Environment:** Google Colab
- **Libraries:** Pandas, NumPy, Seaborn, Matplotlib, Scikit-Learn

## 📈 Key Insights from EDA & Feature Engineering
1. **Smoking Impact:** The `is_smoker` feature shows an exceptionally high positive correlation (**0.787**) with insurance charges. Smoking is the single largest driver of premium costs.
2. **Age & BMI:** Insurance charges show a steady linear increase as age climbs and BMI increases.
3. **Feature Selection:** Based on Pearson Correlation and Chi-Square contingency tests, the final model utilizes `age`, `bmi`, `children`, `is_female`, `is_smoker`, `region_southeast`, and `bmi_category_Obese` as primary predictors.

## 🚀 Future Scope (Work in Progress)
- [ ] Implement a Log Transformation on the target variable (`charges`) to fix non-linear patterns.
- [ ] Experiment with advanced tree-based algorithms like **Random Forest Regressor** and **XGBoost**.
- [ ] Create an explicit feature interaction column for `is_smoker` * `bmi_category_Obese` to better capture combined high-risk premiums.
