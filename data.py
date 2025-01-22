from imports import *

class CircularBuffer:
    """1D circular buffer"""

    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer = np.zeros(capacity, dtype=float)
        self.head = 0

    def append(self, value):
        """Append new element to buffer"""
        self.buffer[self.head] = value
        self.head = (self.head + 1) % self.capacity

    def get(self):
        """Roll buffer and return"""
        return np.roll(self.buffer, -self.head)


class DynoModel(QtCore.QAbstractListModel):
    def __init__(self, *args, **kwargs):
        super(DynoModel, self).__init__(*args, **kwargs)
        
        # Buffers to store latest values 
        self.rpmBuffer = CircularBuffer(480)
        self.trqBuffer = CircularBuffer(480)
        self.pwrBuffer = CircularBuffer(480)
        
        # RPM, TRQ, PWR
        self.latestDynoStats = [0,0,0]
        self.driveRatio = 1
        self.cutoffRPM = 15000

    # Required by qAbstractListModel. 
    # View objects will call data function to populate views
    # Will automatically iterate through calling each index (reason index is parameter)
    # Object requesting data will give role, allowing for function to return differently based on requester

    # DATA FORMAT
    # RPM TRQ HP UNIT
    # int float float string
    # EX:
    # 10  12.2  12.4  IMP | MET
    # 

    def data(self, index, role):
        if role == QtCore.Qt.DisplayRole:
            stat = self.latestDynoStats[index.row()]
            return stat

    def rowCount(self, index):
        return len(self.latestDynoStats)

    def getRPM(self):
        return self.latestDynoStats[0]
    
    def setRPM(self, val):
        self.latestDynoStats[0] = val
    
    def getTRQ(self):
        return self.latestDynoStats[1]
    
    def setTRQ(self, val):
        self.latestDynoStats[1] = val
    
    def getPWR(self):
        return self.latestDynoStats[2]
    
    def setPWR(self, val):
        self.latestDynoStats[2] = val