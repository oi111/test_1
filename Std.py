
import numpy as np
import Data


class RoadStdInfo:
    roadstd=[]
    timestd=[]
    roadstdone = []
    timestdone = []
    def __init__(self):
        self.roadstd = np.zeros([1000000, 3])
        self.timestd=np.zeros([10000, 3])
        self.roadstdone = np.zeros([1000000, 3])
        self.timestdone = np.zeros([10000, 3])
    def process(self,his):
        self.parseRoadInfo(his)
        self.parseTimeInfo(his)
    def parseRoadInfo(self,his):
        for p in his:
            if p.label == 1 or p.label == 2 or p.label == 3:
                self.roadstd[p.linkid][p.label - 1] = self.roadstd[p.linkid][p.label - 1] + 1
                d[p.current_slice_id][p.label - 1] = d[p.current_slice_id][p.label - 1] + 1
    def parseTimeInfo(self,his):
        for p in his:
            if p.label == 1 or p.label == 2 or p.label == 3:
                self.timestd[p.current_slice_id][p.label - 1] = self.timestd[p.current_slice_id][p.label - 1] + 1
    def cal(self):
        for i in range(len(self.roadstd)):
            for j in range(3):
                self.roadstdone[i][j]=self.roadstd[i][j]/(self.roadstd[i][0]+self.roadstd[i][1]+self.roadstd[i][2]+1e-8)
        for i in range(len(self.timestd)):
            for j in range(3):
                self.timestdone[i][j] = self.timestd[i][j] / (
                            self.timestd[i][0] + self.timestd[i][1] + self.timestd[i][2] + 1e-8)



class HisData:
    linkid=0
    label=0
    pdate=0
    current_slice_id = 0
    future_slice_id = 0
    def __init__(self, line,pindex):
        self.pdate=pindex
        a=line.split(';')
        b=a[0].split(' ')
        self.linkid=int(b[0])
        self.label=int(b[1])
        self.current_slice_id=int(b[2])
        self.future_slice_id=int(b[3])

def readHisData(filename,pindex):
    example=[]
    print(filename)
    f=open(filename,"r")
    index=0
    while True:
        line=f.readline()
        if line:
            index=index+1
            example.append(HisData(line,pindex))
        else:
            break
    f.close()
    print('have  readHisData')
    return example
def readAllHisData(filename):
    example=[]
    r=RoadStdInfo()

    for i in range(1,31,1):
        if i<10:
            fn=filename+'0'+str(i)+'.txt'
        else:
            fn=filename+str(i)+'.txt'
        tmp=readHisData(fn,i)
        r.process(tmp)
    r.cal()
    return r