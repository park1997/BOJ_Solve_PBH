# 기본적인 모듈 import
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

from sklearn.ensemble import AdaBoostClassifier, VotingClassifier

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import f1_score, accuracy_score

from sklearn.naive_bayes import GaussianNB, BernoulliNB, MultinomialNB

from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import GradientBoostingClassifier

from sklearn.utils import shuffle

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

from imblearn.over_sampling import SMOTE

train = pd.read_csv("train.csv")
test = pd.read_csv("test.csv")


train.loc[train['target'] == "positive", 'new_target'] = 1
train.loc[train['target'] == "negative", 'new_target'] = 0

positive_train = train[train["new_target"] == 1]
negative_train = train[train["new_target"] == 0]

p_X_train, p_X_test, p_y_train, p_y_test = train_test_split(positive_train.iloc[:,2:1001], positive_train.iloc[:,-1], test_size=0.33, random_state=42)

n_X_train, n_X_test, n_y_train, n_y_test = train_test_split(negative_train.iloc[:,2:1001], negative_train.iloc[:,-1], test_size=0.33, random_state=42)

X_train = pd.concat([p_X_train, n_X_train])
X_train = shuffle(X_train)

X_test = pd.concat([p_X_test, n_X_test])
X_test = shuffle(X_test)

y_train = pd.concat([p_y_train, n_y_train])
y_train = shuffle(y_train)

y_test = pd.concat([p_y_test, n_y_test])
y_test = shuffle(y_test)


# # 검증 데이터나 테스트 데이터가 아닌 학습데이터에서만 오버샘플링 사용할 것
smote = SMOTE(random_state=11)
X_train_over, y_train_over = smote.fit_sample(X_train, y_train)
