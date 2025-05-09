# -*- coding: utf-8 -*-
"""21-03-2025(2311CS020412)

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1ZysV1RCWk9cRalsJY0UZxVzfC9CSYnVE
"""

#SVM classification
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.preprocessing import StandardScaler
from sklearn import svm
from sklearn.svm import SVC
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split, cross_val_score
import matplotlib.pyplot as plt
import seaborn as sns

filename='/content/pima-indians-diabetes.data.csv'
names=['preg','plas','pres','skin','test','mass','pedi','age','class']
dataframe=pd.read_csv(filename,names=names)
array=dataframe.values
X=array[:,0:8]
Y=array[:,8]

X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.3)

X_train.shape,Y_train.shape,X_test.shape,Y_test.shape

#Grid search CV

clf=SVC()
param_grid=[{'kernel':['rbf'],'gamma':[50,5,10,0.5],'C':[15,14,13,12,11,10,0.1,0.001]}]
gsv=GridSearchCV(clf,param_grid,cv=10)
gsv.fit(X_train,Y_train)

gsv.best_params_,gsv.best_score_

clf=SVC(C=15,gamma=50)
clf.fit(X_train,Y_train)
y_pred=clf.predict(X_test)
acc=accuracy_score(Y_test,y_pred)*100
print('Accuracy=',acc)
confusion_matrix(Y_test,y_pred)

