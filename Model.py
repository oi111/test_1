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
        self.model = XGBClassifier(n_estimators=250, max_depth=_max_depth, learning_rate=_learning_rate,
                                  objective='multi:softmax', subsample=_subsample, colsample_bytree=_colsample_bytree,num_class=3)
        #print(self.model)
    def train(self,trainX,trainY,valX,valY):
        print(trainX[0],trainY[0])
        print(valX[0],valY[0])
        #self.model.fit(trainX, trainY,eval_set=[(valX,valY)], eval_metric='error', verbose=True)
        for i in range(len(valY)):
            if valY[i]>3:
                print(i,valY[i])
        print('----------------------')
        for i in range(len(trainY)):
            if trainY[i]>3:
                print(i,trainY[i])
        self.model.fit(np.array(trainX), np.array(trainY),eval_set=[(np.array(valX),np.array(valY))],eval_metric='merror', verbose=True)
        print('have train')
    def test(self,testX,testY):
        y_pred = self.model.predict_proba(np.array(testX))#[:, 2]
        #print(y_pred)
        #print(testY)
        for i in range(100):
            print(y_pred[i],testY[i])
        #y_pred = model.predict(feature)
        return y_pred

#from sklearn import datasets
#from sklearn.model_selection import train_test_split
#from sklearn.metrics import accuracy_score
#from xgboost import XGBClassifier
#md=Model_XGBboost()
_max_depth = 8
_learning_rate = 0.01
_subsample = 0.7
_colsample_bytree = 0.7
#model=XGBClassifier(n_estimators=500, max_depth=_max_depth, learning_rate=_learning_rate,
 #                                 objective='multi:softmax', subsample=_subsample, colsample_bytree=_colsample_bytree,num_class=6)

#digits = datasets.load_digits()

#x_train, x_test, y_train, y_test = train_test_split(digits.data,digits.target,test_size=0.3,random_state=33)

#trainX=np.array([[1,2,3,4],[2 ,3, 4, 5]])
#trainY=np.array([2,1])
#eval_set=[(x_train,y_train)]
#print(trainX)
#print(eval_set)
#print(trainX)
#print(trainY)

#print(x_train)
#print(y_train)
#model.fit(x_train,y_train,eval_set=[(x_train, y_train)],eval_metric='error', verbose=True)
#model.fit(x_train,y_train,eval_set=[(x_train,y_train)],eval_metric='merror', verbose=True)
#print(model)
#from sklearn import preprocessing
#lbl = preprocessing.LabelEncoder()
#testy=[1,2,3]
#trainy = lbl.fit_transform(testy)
#print(trainy)