

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
        self.road_label=float(b[2])
        self.num=float(b[3])
        #print(time,speed)
    def __init__(self,line):
        #time,speed,eta_speed,road_label,num=\
        #print(line)
        self.processData(line)
        #print(self.time, self.speed,self.eta_speed,self.road_label,self.num)
#p=SlideData('230:38.20,32.70,1,15')
#p.processData('230:38.20,32.70,1,15')



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
       # print(a[0])
        #print(b)
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
       # print(self.linkid,self.label,self.current_slice_id,self.future_slice_id)

#f=HisData('516999 1 209 230;205:32.20,28.20,1,4 206:28.40,26.70,1,4 207:26.90,23.90,1,7 208:26.60,23.90,1,7 209:27.70,23.60,1,6;230:35.10,29.80,1,14 231:34.40,29.10,1,15 232:34.70,28.50,1,12 233:33.80,28.20,1,7 234:33.60,25.60,1,4;230:38.20,32.70,1,15 231:37.50,33.80,1,17 232:36.30,34.70,1,14 233:35.40,37.70,1,11 234:34.30,33.50,1,10;230:42.10,29.40,1,11 231:42.00,29.80,1,11 232:38.20,29.90,1,11 233:33.60,30.30,1,8 234:32.80,30.60,1,9;230:34.70,31.10,1,12 231:38.00,34.30,1,13 232:39.40,34.20,1,14 233:40.50,29.10,1,9 234:37.40,30.80,1,8')


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
            #example.append(HisData(line))
            index=index+1
          #  print(index)
            if index%31==0:
                example.append(HisData(line,pindex))
        else:
            break
    f.close()
    print('have  readHisData')
    return example
def readAllHisData(filename):
    example=[]
    for i in range(1,31):
        if i<10:
            fn=filename+'0'+str(i)+'.txt'
        else:
            fn=filename+str(i)+'.txt'
        tmp=readHisData(fn,i)
        #print(tmp)
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
#def testData()
#readExample('20190701.txt')
#print('hello world')
#r=RoadInformation(1,2,3,4,5,6,7,8,9)
#a=readRoadLinkInformation('input/roadlink.txt')
#b=readRoadInformation('input/roadinformation.txt')
#print(a[0].link,a[250000].link)
#print(b[0].speedlimit,b[250000].speedlimit)
