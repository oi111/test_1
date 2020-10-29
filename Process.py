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


def weighted_f1_score(label_data, pred_data):
    f1 = f1_score(y_true=label_data, y_pred=pred_data, average=None)
    f1 = 0.2 * f1[0] + 0.2 * f1[1] + 0.6 * f1[2]
    return f1


def SplitData():
    trainset = []
    testset = []
    return trainset, testset


def getData():
    trainset = []
    testset = []

    trainset,testset=SplitData(data)
    return trainset, testset


def process():
    trainset, testset = getData()
    model = getModel('1')
    Train(model, trainset)
    Test(model, testset)


def getModel(model_name):
    model = ''
    if model_name == '1':
        print(1)
    if model_name == '2':
        print(2)
    Train(model, trainset)
    Test(model, testset)


def Train(model, trainset):
    model.train(trainset)

def Test(model,testset):
    ans=model.test(testset)

