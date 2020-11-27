

class SlideData:
    time=0
    speed=0
    eta_speed=0
    road_label=0
    num=0
    def processData(self,line):
        a=line.split(':')
        b=a[1].split(',')
        self.time=int(a[0])
        self.speed=float(b[0])
        self.eta_speed=float(b[1])
        self.road_label=int(b[2])
        self.num=float(b[3])
        #print(time,speed)
    def __init__(self,line):
        self.processData(line)

class HisData:
    linkid=0
    label=0
    current_slice_id=0
    future_slice_id=0
    recent_feature=[]
    history_feature=[]
    pdate=0
    def __init__(self, line,pindex):
        self.pdate=pindex
        a=line.split(';')
        b=a[0].split(' ')
        self.linkid=int(b[0])
        self.label=int(b[1])
        self.current_slice_id=int(b[2])
        self.future_slice_id=int(b[3])
        self.recent_feature=[]
        self.history_feature=[]
        c = a[1].split(' ')
        for s in c:
            self.recent_feature.append(SlideData(s))
        for i in range(2,6):
            c=a[i].split(' ')
            for s in c:
                self.history_feature.append(SlideData(s))

class RoadInformation:
    linkid=0
    length=0
    direction=0
    pathclass=0
    speedclass=0
    lanenum=0
    speedlimit=0
    level=0
    width=0

    def __init__(self, line):
        if line!='':
            a=line.split()
            self.linkid=int(a[0])
            self.length=int(a[1])
            self.direction=int(a[2])
            self.pathclass=int(a[3])
            self.speedclass=int(a[4])
            self.laneum=int(a[5])
            self.speedlimit=float(a[6])
            self.level=int(a[7])
            self.width=int(a[8])
        else:
            tmp=1

class RoadLinkeInformation():
    link=[]
    index=0
    def __init__(self,line):
        if line!='':
            a=line.split('\t')
            self.index=int(a[0])
            b=a[1].split(',')
            self.link=[]
            for s in b:
                self.link.append(int(s))
        else:
            self.index = 0
            self.link = []

def readRoadInformation(filename):
    f = open(filename, "r")
    index = 0
    roadinfo=[RoadInformation('') for i in range(700000)]
    while True:
        line = f.readline()
        if line:
            tmp=RoadInformation(line)
            roadinfo[tmp.linkid]=tmp
            index = index + 1
        else:
            break
    f.close()
    print('readRoadInformation')
    return roadinfo
def readRoadLinkInformation(filename):
    f = open(filename, "r")
    index = 0
    roadlink=[RoadLinkeInformation('') for i in range(700000)]
    while True:
        line = f.readline()
        if line:
            tmp=RoadLinkeInformation(line)
            roadlink[tmp.index]=tmp
            index = index + 1
        else:
            break
    f.close()
    print('readRoadLinkInformation')
    return roadlink

def readHisData(filename,pindex):
    example=[]
    print(filename)
    f=open(filename,"r")
    index=0
    while True:
        line=f.readline()
        if line:
            index=index+1
            if index%31==0:
                example.append(HisData(line,pindex))
        else:
            break
    f.close()
    print('have  readHisData')
    return example
def readAllHisData(filename):
    example=[]
    for i in range(1,31,1):
        if i<10:
            fn=filename+'0'+str(i)+'.txt'
        else:
            fn=filename+str(i)+'.txt'
        tmp=readHisData(fn,i)
        for p in tmp:
            example.append(p)

    print('have  readAllHisData')
    return example
def readData(fileRoadLink,fileRoadInfo,fileHisData):
    print('begin read data')
    roadlink=readRoadLinkInformation(fileRoadLink)
    roadinfo=readRoadInformation(fileRoadInfo)
    his=readAllHisData(fileHisData)
    return roadlink,roadinfo,his

