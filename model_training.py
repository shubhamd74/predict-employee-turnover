# -*- coding: utf-8 -*-
"""model training.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ztdU-0qXCkFoaAGyJ490r8dr8z-55OKg
"""

# Commented out IPython magic to ensure Python compatibility.
#import required libraries
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns
# %matplotlib inline

from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix

"""# Data Preparation and Feature Engineering"""

# loading dataset from drive folder 
data = pd.read_csv("Employee Turnover.csv")
print(data, "\n")

data.head()

data.isnull().sum()

# Count of students of each class
sns.countplot(data['salary'])

# Count of students of each class
sns.countplot(data['department'])

# Student class by gender
sns.countplot(x='department',hue='salary',data=data,palette='coolwarm')

# Countplot based on the student Class
sns.pairplot(data,hue='salary')

from sklearn import preprocessing
le = preprocessing.LabelEncoder()

le.fit(data['salary'])

data['salary'] = le.fit_transform(data['salary'])

data['department'] = le.fit_transform(data['department'])

data.head()

y= data['quit']

data.drop(['quit'],axis=1, inplace =True)

X = data

X.head()

#Standardize the dataset using standard scaler
scaler = StandardScaler()     # 0.8, 0.5,2,150,3,0,0,6,1
scaler.fit(X)
scaled = scaler.transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=42)

"""# Logistic Regression"""

from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression

log = LogisticRegression(random_state=5)

log.fit(X_train, y_train)

y_pred = log.predict(X_test)

print("Testing Accuracy ",accuracy_score(y_test, y_pred))

print('Logistic Regression Classifier' + '\n')
print(classification_report(y_test,y_pred))

print('\n')

print('Confusion matrix')
sns.heatmap(confusion_matrix(y_test,y_pred),cmap='YlGn_r',annot=True,fmt='g')

"""# SVM Classifier"""

from sklearn import svm
svm_clf = svm.SVC()

svm_clf.fit(X_train, y_train)

y_pred_svm = svm_clf.predict(X_test)

print("Testing Accuracy ",accuracy_score(y_test, y_pred_svm))

print('SVM Classifier' + '\n')
print(classification_report(y_test,y_pred_svm))

print('\n')

print('Confusion matrix')
sns.heatmap(confusion_matrix(y_test,y_pred_svm),cmap='YlGn_r',annot=True,fmt='g')

"""# Decision Tree"""

from sklearn.tree import DecisionTreeClassifier

DTree = DecisionTreeClassifier(max_depth=5)

DTree.fit(X_train,y_train)

y_train_pred = DTree.predict(X_train) 
print("Training Accuracy ",accuracy_score(y_train, y_train_pred))

y_train_predict = DTree.predict(X_test)
DTree.fit(X_test,y_test)

print("Testing Accuracy ",accuracy_score(y_test,y_train_predict))

print('Decision Tree Classifier' + '\n')
print(classification_report(y_test,y_train_predict))

print('\n')

print('Confusion matrix')
sns.heatmap(confusion_matrix(y_test,y_train_predict),cmap='YlGn_r',annot=True,fmt='g')

# import pickle
# pickle_out = open("classifier.pkl","wb")
# pickle.dump(DTree, pickle_out)
# pickle_out.close()

input_f = np.array([0.8,0.5,2,150,3,0,0,6,1])
input_f = input_f.reshape(1,-1)

df = pd.DataFrame(input_f, columns = ['satisfaction_level','last_evaluation','number_project','average_montly_hours','time_spend_company','Work_accident','promotion_last_5years','department','salary'])



df.head()

y_train_pred2 = DTree.predict(df)

y_train_pred2



