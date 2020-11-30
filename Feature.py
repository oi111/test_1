
import Data

class Example:
    feature=[]
    label=0
    def __init__(self):
        self.feature=[]
        self.label=0
    def getOneHot(self,val,tot):
        tmp=[0 for i in range(tot)]
        tmp[val]=1
        return tmp
    def AddFeature_RoadInfo(self, r):
        self.feature.append(r.length)

        tmp=self.getOneHot(r.direction,4)
        for p in tmp:
            self.feature.append(p)

        tmp=self.getOneHot(r.pathclass,6)
        for p in tmp:
            self.feature.append(p)

        tmp=self.getOneHot(r.speedclass,9)
        for p in tmp:
            self.feature.append(p)


        self.feature.append(r.lanenum)

        self.feature.append(r.speedlimit)

        tmp=self.getOneHot(r.level,6)
        for p in tmp:
            self.feature.append(p)
        #self.feature.append(r.level)
        self.feature.append(r.width)
    def AddFeature_His(self,r):
        self.feature.append(r.current_slice_id)
        self.feature.append(r.future_slice_id)
        for p in r.recent_feature:
            self.feature.append(p.speed)
            self.feature.append(p.eta_speed)
            #self.feature.append(p.road_label)
            tmp=self.getOneHot(p.road_label, 5)
            for q in tmp:
                self.feature.append(q)

        for p in r.history_feature:
            self.feature.append(p.speed)
            self.feature.append(p.eta_speed)
            #self.feature.append(p.road_label)
            tmp=self.getOneHot(p.road_label, 5)
            for q in tmp:
                self.feature.append(q)
        self.label=r.label-1

    def AddFeature_Date(self,pdate):
        tmp=[0,0,0,0,0,0,0]
        tmp[pdate%7]=1
        for p in tmp:
            self.feature.append(p)
    def AddFeature_Time(self,r2):
        self.feature.append(r2[0])
        self.feature.append(r2[1])
        self.feature.append(r2[2])
        #print(r2[0],r2[1],r2[2])
    def AddFeature(self,h1,r1,r2):
        #print(r1)
        #print(r1.pathclass)
        self.AddFeature_His(h1)
        self.AddFeature_RoadInfo(r1)
        self.AddFeature_Date(h1.pdate)
        #self.AddFeature_Time(r2)
        #AddFeature_RoadInfo()
        #AddFeature_His(h1)
        #print('have end addfeature')

