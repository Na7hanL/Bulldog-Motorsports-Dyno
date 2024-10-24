from imports import *

def getRandomNums():
    return random.randint(0,100)


class DynoModel(QtCore.QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(DynoModel, self).__init__(*args, **kwargs)
        # RPM, TRQ, PWR
        self.dynoStats = [0,0,0]

    # Required by qAbstractListModel. 
    # View objects will call data function to populate views
    # Will automatically iterate through calling each index (reason index is parameter)
    # Object requesting data will give role, allowing for function to return differently based on requester

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            stat = self.dynoStats[index.row()]
            return stat

    def rowCount(self, index):
        return len(self.dynoStats)

    def getRPM(self):
        return str(self.dynoStats[0])
    
    def getTRQ(self):
        return str(self.dynoStats[1])
    
    def getPWR(self):
        return str(self.dynoStats[2])