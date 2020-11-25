
import Data

class Example:
    feature=[]
    label=0
    def __init__(self):
        self.feature=[]
        self.label=0
    def AddFeature_RoadInfo(self, r):
        #print('AddFeature_RoadInfo')
        #print(r)
        #print(r.pathclass)
        self.feature.append(r.length)
        self.feature.append(r.direction)
        self.feature.append(r.pathclass)
        self.feature.append(r.speedclass)
        self.feature.append(r.lanenum)
        self.feature.append(r.speedlimit)
        self.feature.append(r.level)
        self.feature.append(r.width)
        #self.feature
    def AddFeature_His(self,r):
        self.feature.append(r.current_slice_id)
        self.feature.append(r.future_slice_id)
        for p in r.recent_feature:
            self.feature.append(p.speed)
            self.feature.append(p.eta_speed)
            self.feature.append(p.road_label)
        for p in r.history_feature:
            self.feature.append(p.speed)
            self.feature.append(p.eta_speed)
            self.feature.append(p.road_label)
        #print(r.label)
        self.label=r.label-1
        #if r.label>=1 and r.label<=3:
         #   self.label[r.label-1]=1
        #else:
         #   print(r.label)
       # print('have end AddFeature_His')
    def AddFeature(self,h1,r1):
        #print(r1)
        #print(r1.pathclass)
        self.AddFeature_His(h1)
        self.AddFeature_RoadInfo(r1)
        #AddFeature_RoadInfo()
        #AddFeature_His(h1)
        #print('have end addfeature')

