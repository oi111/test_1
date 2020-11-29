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
import random
import ProcessTrainData as ptd
import test as te
import Std as st
import pandas as pd


def weighted_f1_score(label_data, pred_data):
    f1 = f1_score(y_true=label_data, y_pred=pred_data, average=None)
    f1 = 0.2 * f1[0] + 0.2 * f1[1] + 0.6 * f1[2]
    return f1
def calLabel(pred_y):
    ret=[]
    print(pred_y)
    for i in range(len(pred_y)):
        if pred_y[i][0]>pred_y[i][1] and pred_y[i][0]>pred_y[i][2]:
            ret.append(0)
        if pred_y[i][1]>pred_y[i][0] and pred_y[i][1]>pred_y[i][2]:
            ret.append(1)
        if pred_y[i][2]>pred_y[i][0] and pred_y[i][2]>pred_y[i][1]:
            ret.append(2)
    return ret


def outputData(finalZ,pred_y):
    a = []
    for i in range(len(finalZ)):
        g = []
        g.append(finalZ[i].linkid)
        g.append(finalZ[i].current_slice_id)
        g.append(finalZ[i].future_slice_id)
        g.append(pred_y[i])
        a.append(g)
    df = pd.DataFrame(a, columns=['link', 'current_slice_id', 'future_slice_id', 'label'])
    df.to_csv('outputData.csv', index=False)
def Train(model, trainX,trainY,valX,valY):
    model.train(trainX,trainY,valX,valY)

def Test(model,testX,testY):
    pred_y=model.test(testX,testY)
    return pred_y

def getModel(model_name):
    model = ''
    if model_name == 'xgb':
        model=md.Model_XGBboost()
    if model_name == '2':
        print(2)
    return model
def process(fileRoadLink,fileRoadInfo,fileHisData,fileFinalData):
    roadlink, roadinfo, his=da.readData(fileRoadLink,fileRoadInfo,fileHisData)
    hisstd=st.readAllHisData(fileHisData)
    trainX,trainY,testX,testY = ptd.getData(roadlink,roadinfo,his,hisstd)
    te.testNullId(his)
    print('========================')
    model = getModel('xgb')
    Train(model, trainX,trainY,testX,testY)
    pred_y=Test(model, testX,testY)
    pred_y=calLabel(pred_y)
    score=weighted_f1_score(testY,pred_y)

    finalX,finalY,finalZ=ptd.getTestData(roadlink, roadinfo, fileFinalData,hisstd)
    pred_y = Test(model, finalX, finalY)
    pred_y = calLabel(pred_y)
    outputData(finalZ,pred_y)
    print(score)





fileRoadLink='input/roadlink.txt'
fileRoadInfo='input/roadinformation.txt'
fileHisData='input/201907'
#roadlink, roadinfo, his=da.readData(fileRoadLink,fileRoadInfo,fileHisData)
#trainX,trainY,testX,testY = getData(roadlink,roadinfo,his)
#process(fileRoadLink,fileRoadInfo,fileHisData)
#data=buildExample(roadlink,roadinfo,his)
#trainset,testset=SplitData(data)
#print(len(trainset),len(testset))
#trainset, testset = getData(roadlink,roadinfo,his)

#e=ft.Example()

#roadlink[0].link
#print((ft.Example)(roadlink[0]).linkid)
#print(roadlink[0].length)
#print(roadlink[0])

#e.AddFeature_RoadInfo(roadinfo[0])
#e.AddFeature_His(his[0])
#e.AddFeature(roadinfo[0],his[0])
#print(len(roadlink),len(roadinfo),len(his))