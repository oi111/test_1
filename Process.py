from sklearn.svm import SVC
from sklearn.metrics import f1_score
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import MultiLabelBinarizer
import tensorflow as tf
from sklearn.cluster import KMeans
from sklearn.metrics import roc_auc_score, average_precision_score
import numpy as np
from sklearn.linear_model import SGDClassifier

import Data as da
import Feature as ft


def weighted_f1_score(label_data, pred_data):
    f1 = f1_score(y_true=label_data, y_pred=pred_data, average=None)
    f1 = 0.2 * f1[0] + 0.2 * f1[1] + 0.6 * f1[2]
    return f1


def SplitData(data):
    trainset = []
    testset = []
    for i in range(int(len(data)*0.8)):
        trainset.append(data[i])
    for i in range(int(len(data)*0.8),int(len(data)*1)):
        testset.append(data[i])
    return trainset, testset
def buildExample(roadlink,roadinfo,his):
    ret=[]
    for h in his:
        e=ft.Example()
        e.AddFeature(h,roadinfo[h.linkid])
        ret.append(e)
    print(len(ret))
    print('have end buildExample')
    return ret

def getData(roadlink,roadinfo,his):
    trainset = []
    testset = []
    data=buildExample(roadlink,roadinfo,his)
    trainset,testset=SplitData(data)
    return trainset, testset

def Train(model, trainset):
    model.train(trainset)

def Test(model,testset):
    ans=model.test(testset)


def getModel(model_name):
    model = ''
    if model_name == '1':
        model=Model_XGBboost()
    if model_name == '2':
        print(2)
    Train(model, trainset)
    Test(model, testset)
def process(fileRoadLink,fileRoadInfo,fileHisData):
    roadlink, roadinfo, his=readData(fileRoadLink,fileRoadInfo,fileHisData)
    trainset, testset = getData(roadlink,roadinfo,his)
    model = getModel('1')
    Train(model, trainset)
    Test(model, testset)

fileRoadLink='input/roadlink.txt'
fileRoadInfo='input/roadinformation.txt'
fileHisData='input/20190701.txt'
roadlink, roadinfo, his=da.readData(fileRoadLink,fileRoadInfo,fileHisData)


#data=buildExample(roadlink,roadinfo,his)
#trainset,testset=SplitData(data)
#print(len(trainset),len(testset))
trainset, testset = getData(roadlink,roadinfo,his)
#e=ft.Example()

#roadlink[0].link
#print((ft.Example)(roadlink[0]).linkid)
#print(roadlink[0].length)
#print(roadlink[0])

#e.AddFeature_RoadInfo(roadinfo[0])
#e.AddFeature_His(his[0])
#e.AddFeature(roadinfo[0],his[0])
#print(len(roadlink),len(roadinfo),len(his))