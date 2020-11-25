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
import Model as md


def weighted_f1_score(label_data, pred_data):
    f1 = f1_score(y_true=label_data, y_pred=pred_data, average=None)
    f1 = 0.2 * f1[0] + 0.2 * f1[1] + 0.6 * f1[2]
    return f1


def SplitData(data):
    trainX= []
    trainY=[]
    testX = []
    testY=[]
    for i in range(int(len(data)*0.8)):
        trainX.append(data[i].feature)
        trainY.append(data[i].label)
    for i in range(int(len(data)*0.8),int(len(data)*1)):
        testX.append(data[i].feature)
        testY.append(data[i].label)
    return trainX,trainY,testX,testY
def buildExample(roadlink,roadinfo,his):
    ret=[]
    #retY=[]
    for h in his:
        e=ft.Example()
        e.AddFeature(h,roadinfo[h.linkid])
        ret.append(e)
        #tmp=[0,0,0]
        #tmp[e.label]=1
        #retY.append(tmp)
    print(len(ret))
    print('have end buildExample')
    return ret

def getData(roadlink,roadinfo,his):
    trainset = []
    testset = []
    data=buildExample(roadlink,roadinfo,his)
    trainX,trainY,testX,testY=SplitData(data)
    return trainX,trainY,testX,testY

def Train(model, trainX,trainY,valX,valY):
    model.train(trainX,trainY,valX,valY)

def Test(model,testX,testY):
    ans=model.test(testX,testY)



def getModel(model_name):
    model = ''
    if model_name == 'xgb':
        model=md.Model_XGBboost()
    if model_name == '2':
        print(2)
    return model
def process(fileRoadLink,fileRoadInfo,fileHisData):
    roadlink, roadinfo, his=da.readData(fileRoadLink,fileRoadInfo,fileHisData)
    trainX,trainY,testX,testY = getData(roadlink,roadinfo,his)
    print('========================')
    model = getModel('xgb')
    Train(model, trainX,trainY,testX,testY)
    Test(model, testX,testY)





fileRoadLink='input/roadlink.txt'
fileRoadInfo='input/roadinformation.txt'
fileHisData='input/20190701.txt'
#roadlink, roadinfo, his=da.readData(fileRoadLink,fileRoadInfo,fileHisData)
#trainX,trainY,testX,testY = getData(roadlink,roadinfo,his)
process(fileRoadLink,fileRoadInfo,fileHisData)
#data=buildExample(roadlink,roadinfo,his)
#trainset,testset=SplitData(data)
#print(len(trainset),len(testset))
#trainset, testset = getData(roadlink,roadinfo,his)
b=[0,0,0]
print(b)
#e=ft.Example()

#roadlink[0].link
#print((ft.Example)(roadlink[0]).linkid)
#print(roadlink[0].length)
#print(roadlink[0])

#e.AddFeature_RoadInfo(roadinfo[0])
#e.AddFeature_His(his[0])
#e.AddFeature(roadinfo[0],his[0])
#print(len(roadlink),len(roadinfo),len(his))