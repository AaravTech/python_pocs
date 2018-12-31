import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 
import seaborn as sns
import statsmodels.api as sm

from sklearn.preprocessing import LabelEncoder, OneHotEncoder, StandardScaler, Imputer
from sklearn.feature_selection import RFE
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix
from sklearn.cross_validation import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.svm import SVC, LinearSVC

# Setting plot configuration
plt.rc("font", size=14)

cat_vars = ["Pclass", "Sex", "Embarked"]
ignore_list = ["PassengerId", "Ticket", "Name", "Cabin"]
sl = 0.05

def load_data():
    data = pd.read_csv("data/train.csv")
    test_input = pd.read_csv("data/test.csv")
    return (data, test_input)

def process_input_data(input_data):
    for var in cat_vars:
        cat_list='var'+'_'+var
        cat_list = pd.get_dummies(input_data[var], prefix=var, drop_first=True)
        data1=input_data.join(cat_list)
        input_data=data1

    var_list = input_data.columns.tolist()
    to_keep=[i for i in var_list if i not in cat_vars + ignore_list]
    final_data = input_data[to_keep]
    final_data_vars = final_data.columns.values.tolist()
    final_data.Age = final_data['Age'].fillna(final_data['Age'].mean())
    final_data.Fare = final_data['Fare'].fillna(final_data['Fare'].mean())
    y = ['Survived']
    X = [i for i in final_data_vars if i not in y]
    return (final_data, X, y)

def filter_features(data, X, y):
    logreg = LogisticRegression()
    rfe = RFE(logreg, 18)
    rfe = rfe.fit(data[X], data[y])
    selected_features = [i[1] for i in zip(rfe.support_.tolist(), X) if i[0]]
    return selected_features

def eliminate_features(x, y, sl):
    vars = x.columns.tolist()
    print(vars)
    for var in vars:
        regressor_OLS = sm.OLS(y, x).fit()
        values = list(regressor_OLS.pvalues)
        maxVar = max(values)
        index = values.index(maxVar)
        if maxVar > sl:
            del x[vars[index]]
            x = eliminate_features(x, y, sl)
    return x


train_data, test_data = load_data()
final_data, X, y = process_input_data(train_data)
input_data, X_t, y_t = process_input_data(test_data)
selected_features = filter_features(final_data, X, y)

X = final_data[selected_features]
y_train = final_data[y]
X_train = eliminate_features(X, y_train, sl)
input_data = input_data[X.columns.tolist()]

# X_train, X_test, y_train, y_test = train_test_split(X_train, y_train, test_size = 0.05, random_state = 0)

model = LogisticRegression()
model.fit(X_train, y_train)
# model = RandomForestClassifier(n_estimators=50)
# model.fit(X_train, y_train)
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
# model = SVC()
# model.fit(X_train, y_train)
y_pred = model.predict(input_data)


print('Accuracy of logistic regression classifier on test set: {:.2f}'.format(model.score(X_train, y_train)*100))

# Output Predicted data
output_df = pd.DataFrame({'PassengerId':test_data.PassengerId.values.tolist(), 'Survived':y_pred})
print(output_df.head())
output_df.to_csv("submission.csv", sep=",", index=False)