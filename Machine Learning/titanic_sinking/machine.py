import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, Imputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix

# --------------------
# Getting data
# --------------------
# Reading train and test data from csv
# --------------------
train_df = pd.read_csv("data/train.csv")
test_df = pd.read_csv("data/test.csv")
predict_df = pd.read_csv("data/gender_submission.csv")

# --------------------
# Data preprocessing
# --------------------
# 1. Filtering data as per required features
# --------------------
X_train = train_df.loc[:, ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]]
Y_train = train_df.loc[:, ["Survived"]]

X_test = test_df.loc[:, ["Pclass", "Sex", "Age", "SibSp", "Parch", "Fare"]]
Y_test = predict_df.loc[:, ["Survived"]]

# Reshaping Prediction data
Y_train = Y_train.reshape

# 2. Processing categorical data
# --------------------
label_encoder = LabelEncoder()
X_train.Sex = label_encoder.fit_transform(X_train.Sex).astype('str')
X_test.Sex = label_encoder.fit_transform(X_test.Sex).astype('str')

# 3. Fill missing data
# --------------------
imputer = Imputer(missing_values='NaN', strategy='mean', axis=0)
X_train = imputer.fit_transform(X_train)
X_test = imputer.fit_transform(X_test)

# 4. Feature scaling
# --------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.fit_transform(X_test)

# --------------------
# Regression
# --------------------
regressor = LogisticRegression()
regressor.fit(X_train, Y_train)
y_test = regressor.predict(X_test)

# --------------------
# Plotting result
# --------------------
c_matrix = confusion_matrix(Y_test, y_test)
accuracy = c_matrix.diagonal().sum() * 100 / c_matrix.sum()
print("Accuracy of prediction %.3f" % (accuracy))