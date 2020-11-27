

import numpy as np

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
       # print(a[0])
        #print(b)
        self.linkid=int(b[0])
        self.label=int(b[1])
        self.current_slice_id=int(b[2])
        self.future_slice_id=int(b[3])
        #print(self.linkid,self.label)

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
            #if index%31==0:
            example.append(HisData(line,pindex))
        else:
            break
    f.close()
    print('have  readHisData')
    return example
def readAllHisData(filename):
    example=[]
    a = np.zeros([1000000, 3])
    b=np.zeros(1000000)
    c = np.zeros(10000)
    d=np.zeros([10000, 3])
    for i in range(1,31,1):
        if i<10:
            fn=filename+'0'+str(i)+'.txt'
        else:
            fn=filename+str(i)+'.txt'
        tmp=readHisData(fn,i)
        #print(tmp)
        for p in tmp:
            #print(p.linkid,p.label)
            b[p.linkid]=b[p.linkid]+1
            c[p.current_slice_id]=c[p.current_slice_id]+1
            c[p.future_slice_id]=c[p.future_slice_id]+1
            if p.label == 1 or p.label == 2 or p.label == 3:
                a[p.linkid][p.label - 1] = a[p.linkid][p.label - 1] + 1
                d[p.current_slice_id][p.label - 1] = d[p.current_slice_id][p.label - 1] + 1
            #example.append(p)

    print('have  readAllHisData')
    t2=0
    for i in range(len(b)):
        if b[i]>0:
            t2=t2+1
            print(i,b[i])
    print('ALL: ',t2)
    t4=0
    for i in range(len(c)):
        if c[i]>0:
            print(i,c[i])
            t4=t4+1
    print('Time:',t4)
    tot = 0
    t1=0
    t3=0
    for p in a:
        if p[1] == 0 and p[2] == 0:
            tot = tot + 1
        if p[0]>0:
            t1=t1+1
        if p[0]/(p[0]+p[1]+p[2]+1e-8)>0.95:
            t3=t3+1
    print('NULL point: ',tot,t1,t3)

    tot = 0
    t1 = 0
    t3 = 0
    for p in d:
        if p[1] == 0 and p[2] == 0:
            tot = tot + 1
        if p[0] > 0:
            t1 = t1 + 1
        if p[0] / (p[0] + p[1] + p[2] + 1e-8) > 0.95:
            t3 = t3 + 1
    print('NULL point: ', tot, t1, t3)
    return example
readAllHisData('input/201907')

