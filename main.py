# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

import Process as pr
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    fileRoadLink='input/roadlink.txt'
    fileRoadInfo='input/roadinformation.txt'
    fileHisData='input/201907'
    finalData=''
#roadlink, roadinfo, his=da.readData(fileRoadLink,fileRoadInfo,fileHisData)
#trainX,trainY,testX,testY = getData(roadlink,roadinfo,his)
    pr.process(fileRoadLink,fileRoadInfo,fileHisData,finalData)
# See PyCharm help at https://www.jetbrains.com/help/pycharm/
