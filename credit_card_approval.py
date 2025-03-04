from google.colab import drive
drive.mount('/content/drive')

import numpy as np import pandas as pd import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.preprocessing import scale
from sklearn.linear_model import LinearRegression, LogisticRegression from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix, classification_report, mean_squared_error, r2_score
from sklearn.preprocessing import OneHotEncoder from sklearn import preprocessing
from sklearn.metrics import accuracy_score

# Load data
x = pd.read_csv(r"drive/MyDrive/CreditCard.csv") y=x.copy()

# Convert categorical variables into dummy/indicator variables x = pd.get_dummies(x)

# Logistic Regression model x_train1 = x.drop(columns='Approved')
y_train1 = x['Approved']

x_train, x_valid, y_train, y_valid = train_test_split(x_train1, y_train1, test_size=0.2, random_state=100)

logreg = LogisticRegression()
logreg.fit(x_train, y_train)

y_pred = logreg.predict(x_valid)

accuracy = accuracy_score(y_valid, y_pred) print('Logistic Regression model parameters')
print("Accuracy of the Logistic Regression Model: ", accuracy)

confusion = confusion_matrix(y_valid, y_pred, labels=[1, 0]) print('\nConfusion\n', confusion)

report = classification_report(y_valid, y_pred)
print('\nReport\n', report)

# Linear Regression model
x_train2, x_test2, y_train2, y_test2 = train_test_split(x_train1, y_train1, test_size=0.3, random_state=42)

# Scaling
scaler = preprocessing.StandardScaler()
scaler.fit(x_train2)
x_train2_scaled = scaler.transform(x_train2)
x_test2_scaled = scaler.transform(x_test2)

# Training
regressor = LinearRegression()
regressor.fit(x_train2_scaled, y_train2)

# Prediction
y_pred2 = regressor.predict(x_test2_scaled)

# Evaluation
print('Linear Regression model parameters')
print('\nMean Squared error: %.2f' % mean_squared_error(y_test2, y_pred2)) print('Variance score: %.2f' % r2_score(y_test2, y_pred2))

# ROC Curve
from sklearn.metrics import roc_curve, roc_auc_score

y_proba = logreg.predict_proba(x_valid)[:, 1]
fpr, tpr, thresholds = roc_curve(y_valid, y_proba)

plt.figure(figsize=(8, 6)) plt.plot(fpr, tpr, label='ROC Curve')
plt.plot([0, 1], [0, 1], linestyle='--', label='Random') plt.xlabel('False Positive Rate') plt.ylabel('True Positive Rate') plt.title('ROC Curve') plt.legend()
plt.show()
