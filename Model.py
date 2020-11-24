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
from xgboost import XGBClassifier



class Model_XGBboost:
    model=''
    def __init__(self):
        #model = XGBClassifier()  # 载入模型（模型命名为model)
        #print(1)
        self.initModel()
    def initModel(self):
        _max_depth = 10
        _learning_rate = 0.01
        _subsample = 0.7
        _colsample_bytree = 0.7
        self.model = XGBClassifier(n_estimators=500, max_depth=_max_depth, learning_rate=_learning_rate,
                                  objective='binary:logistic', subsample=_subsample, colsample_bytree=_colsample_bytree)
        print(self.model)
    def train(self,trainX,trainY,testX,testY):
        self.model.fit(trainX, trainY,eval_set=[(testX,testY)], eval_metric='error', verbose=True)
    def test(self,testX):
        y_pred = self.model.predict_proba(X_test)[:, 1]
        #y_pred = model.predict(feature)
        return y_pred


#md=Model_XGBboost()
