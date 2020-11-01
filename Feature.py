

class Example:
    feature=[]
    label=0
    def __init__(self):
        self.feature=[]
        self.label=0
    def AddFeature(self,r1,h1):
        AddFeature_RoadInfo(r1)
        AddFeature_His(h1)
    def AddFeature_RoadInfo(self, r):
        feature.append(r.length)
        feature.append(r.direction)
        feature.append(r.pathclass)
        feature.append(r.speedclass)
        feature.append(r.lanenum)
        feature.append(r.speedlimit)
        feature.append(r.level)
        feature.append(r.width)
        #self.feature
    def AddFeature_His(self,r):
        feature.append(h.current_slice_id)
        feature.append(h.future_slice_id)
        for p in r.recent_feature:
            feature.append(p.speed)
            feature.append(p.eta_speed)
            feature.append(p.road_label)
        for p in r.history_feature:
            feature.append(p.speed)
            feature.append(p.eta_speed)
            feature.append(p.road_label)