
import Data as dt
import Feature
import Feature as ft
import random
import test as te

def calBiLi2(data):
    t0=0
    t1=0
    t2=0
    for i in range(len(data)):
        if data[i]==0:
            t0=t0+1
        if data[i]==1:
            t1=t1+1
        if data[i]==2:
            t2=t2+1
    print(t0,t1,t2)
def calBiLi(data):
    t0=0
    t1=0
    t2=0
    for i in range(len(data)):
        if data[i].label==0:
            t0=t0+1
        if data[i].label==1:
            t1=t1+1
        if data[i].label==2:
            t2=t2+1
    print(t0,t1,t2)

def SplitData(data,rate):
    trainX= []
    trainY=[]
    testX = []
    testY=[]
    for i in range(int(len(data)*rate)):
        trainX.append(data[i].feature)
        trainY.append(data[i].label)
    for i in range(int(len(data)*rate),int(len(data)*1)):
        testX.append(data[i].feature)
        testY.append(data[i].label)
    return trainX,trainY,testX,testY
def buildExample(roadlink,roadinfo,his):
    ret=[]
    for h in his:
        e=ft.Example()
        e.AddFeature(h,roadinfo[h.linkid])
        if e.label==0 or e.label==1 or e.label==2:
            ret.append(e)
    print(len(ret))
    print('have end buildExample')
    return ret

def changeBiLi(trainX,trainY):
    px=[]
    py=[]
    for i in range(len(trainY)):
        if trainY[i]==2:
            for j in range(15):
                px.append(trainX[i])
                py.append(trainY[i])
        if trainY[i]==1:
            for j in range(5):
                px.append(trainX[i])
                py.append(trainY[i])
        if trainY[i]==0 or trainY[i]==3:
            px.append(trainX[i])
            py.append(trainY[i])
    return px,py
def randomGet(trainX,trainY):
    px = []
    py = []
    for i in range(len(trainY)):
        if random.random()<0.1:
            px.append(trainX[i])
            py.append(trainY[i])
    return px,py
def randomData(s1,s2):
    for i in range(1000000):
        p1=int(random.random()*len(s1))
        p2=int(random.random()*len(s1))
        if p1!=p2:
            tmp=s1[p1]
            s1[p1]=s1[p2]
            s1[p2]=tmp

            tmp=s2[p1]
            s2[p1]=s2[p2]
            s2[p2]=tmp
    return s1,s2
def processTrainData(trainX,trainY):
    trainX,trainY=changeBiLi(trainX, trainY)
    trainX, trainY = randomGet(trainX, trainY)
    trainX,trainY=randomData(trainX,trainY)
    return trainX,trainY

def getData(roadlink,roadinfo,his):
    trainset = []
    testset = []
    data=buildExample(roadlink,roadinfo,his)
    te.testRoadInformation(roadinfo)
    te.testHisData(his)
    calBiLi(data)
    trainX,trainY,testX,testY=SplitData(data,0.8)
    trainX,trainY=processTrainData(trainX,trainY)
    calBiLi2(trainY)
    return trainX,trainY,testX,testY

def getTestData(roadlink,roadinfo,fileHisData):
    trainset = []
    testset = []
    his = dt.readAllHisData(fileHisData)
    data=buildExample(roadlink,roadinfo,his)
    calBiLi(data)
    finalX,finalY,testX,testY=SplitData(data,1)
    #trainX,trainY=processTrainData(trainX,trainY)
    #calBiLi2(trainY)
    return finalX,finalY