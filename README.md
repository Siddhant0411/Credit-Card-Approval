# Binary Classification: Logistic vs. Linear Regression Analysis

This project implements a binary classification pipeline to predict outcomes using **Logistic Regression**. It features a comparative analysis against **Linear Regression** to demonstrate why classification-specific models are preferred for categorical targets.

---

## 📊 Performance at a Glance

| Metric | Logistic Regression | Linear Regression |
| :--- | :---: | :---: |
| **Accuracy** | 0.80 | N/A |
| **ROC AUC** | 0.89 | N/A |
| **$R^2$ Score** | N/A | 0.40 |
| **MSE** | N/A | 0.15 |



---

## 🛠️ Implementation Details

### Dependencies
The project relies on the following Python libraries:
* **scikit-learn**: Model training and evaluation metrics.
* **matplotlib & seaborn**: Data visualization.
* **numpy & pandas**: Data handling and processing.

---
## 📌 Model Comparison: Logistic vs. Linear Regression

### ✅ Logistic Regression Strengths

- Built specifically for **binary classification**
- Effectively models **class probabilities**
- Strong performance metrics:
  - ROC AUC: **0.89**
  - Accuracy: **0.80**
- High operational reliability:
  - Recall of **0.85** for the positive class
  - Only **19 False Negatives** compared to **59 True Positives**
  - Suitable when minimizing missed positive cases is critical

### ❌ Linear Regression Limitations

- Designed for **continuous targets**, not categories
- Produces values that require arbitrary thresholds
- Low explanatory power:
  - R² score of **0.40**, leaving 60% of variance unexplained
- Poor fit for classification decision boundaries

---

## 📝 Conclusion: Logistic vs. Linear Regression

Based on the comparative metrics, here is the final takeaway for the project:

### 1. Classification is the Right Tool
The high **AUC of 0.89** and **accuracy of 0.80** demonstrate that Logistic Regression is highly effective for this dataset. Unlike linear models, it successfully captures the non-linear decision boundary between classes using the sigmoid function.

### 2. Linear Regression Limitations
The low **$R^2$ of 0.40** indicates that a linear line fails to explain 60% of the data's variance. In this context, predicting a continuous value is significantly less reliable than predicting a category, as linear models can produce predictions outside the $[0, 1]$ range.

### 3. Operational Strength
With a **Recall of 0.85** for the positive class, the model is "safe"—it is highly efficient at not missing positive cases (only 19 False Negatives vs. 59 True Positives).

---

## 🚀 Key Takeaway
> **Logistic Regression** is the mathematically sound choice for this dataset, providing a probabilistic framework that Linear Regression cannot offer for binary targets.
