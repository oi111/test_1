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
        _max_depth = 8
        _learning_rate = 0.01
        _subsample = 0.7
        _colsample_bytree = 0.7
        self.model = XGBClassifier(n_estimators=10, max_depth=_max_depth, learning_rate=_learning_rate,
                                  objective='multi:softmax', subsample=_subsample, colsample_bytree=_colsample_bytree)
        print(self.model)
    def train(self,trainX,trainY,valX,valY):
        print(trainX[0],trainY[0])
        #self.model.fit(trainX, trainY,eval_set=[(valX,valY)], eval_metric='error', verbose=True)
        self.model.fit(trainX, trainY, eval_metric='error', verbose=True)
        print('have train')
    def test(self,testX):
        y_pred = self.model.predict_proba(X_test)[:, 1]
        #y_pred = model.predict(feature)
        return y_pred


#md=Model_XGBboost()
_max_depth = 8
_learning_rate = 0.01
_subsample = 0.7
_colsample_bytree = 0.7
#model=XGBClassifier(n_estimators=500, max_depth=_max_depth, learning_rate=_learning_rate,
 #                                 objective='multi:softmax', subsample=_subsample, colsample_bytree=_colsample_bytree)
#print(model)
#from sklearn import preprocessing
#lbl = preprocessing.LabelEncoder()
#testy=[1,2,3]
#trainy = lbl.fit_transform(testy)
#print(trainy)