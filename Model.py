from sklearn.linear_model import LogisticRegression as LR
from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import tensorflow as tf
from sklearn.cluster import KMeans
from sklearn.metrics import roc_auc_score, average_precision_score
import numpy as np
from sklearn.linear_model import SGDClassifier


class Model_XGBboost:
    model=''
    def __init__(self):
        print(1)
    def initModel(self):
        model=1
    def train(self,feature,label):
        model.fit(feature,label)
    def test(self,feature):
        model.predict(feature)


class Model_XGBboost2:
    model=''
    def __init__(self):
        print(1)
    def initModel(self):
        model=1
    def train(self,feature,label):
        model.fit(feature,label)
    def test(self,feature):
        model.predict(feature)
