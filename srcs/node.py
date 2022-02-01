class Node:
    def __init__(self, nodeName, nodeType, propDelay, setupTime = 0, holdTime = 0):
        self.nodeName = nodeName
        self.nodeType = nodeType
        self.propDelay = propDelay
        self.setupTime = setupTime
        self.holdTime = holdTime
        self.proceedNodes = []
        self.succeedNodes = []
        self.onTheGraph = False

    def getNodeName(self):
        return self.nodeName
    def setNodeName(self,nodeName):
        self.nodeName = nodeName

    def getNodeType(self):
        return self.nodeType
    def setNodeTyoe(self,nodeType):
        self.nodeType = nodeType

    def getPropDelay(self):
        return self.propDelay
    def setPropDelay(self,propDelay):
        self.propDelay = propDelay

    def getSetupTime(self):
        return self.setupTime
    def setSetupTime(self,setupTime):
        self.setupTime = setupTime

    def getHoldTime(self):
        return self.holdTime
    def setHoldTime(self,holdTime):
        self.holdTime = holdTime

