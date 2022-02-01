class Netlist:
    def __init__(self, allNodes = []):
        self.allNodes = allNodes

    def addNode(self, *args):
        if not self.allNodes or args[0] not in self.allNodes:
            self.allNodes.append(args[0])
        if args[1:]:
            for arg in args[1:]:
                if arg not in args  [0].succeedNodes:
                    args[0].succeedNodes.append(arg)
                    arg.proceedNodes.append(args[0])
                    if arg not in self.allNodes:
                        self.allNodes.append(arg)

    def checkFF(self, node, list, allPaths):
        list.append(node)
        if node.nodeType == "FF" and len(list) > 1:
            allPaths.append(list)
        elif not node.succeedNodes:
            pass
        else:
            for node in node.succeedNodes:
                new_list = []
                for node1 in list:
                    new_list.append(node1)
                self.checkFF(node, new_list, allPaths)

    def combPath(self, node, list, allPaths):
        list.append(node)
        if node.nodeType == "FF":
            pass
        elif not node.succeedNodes and node.nodeType == "GATE":
            allPaths.append(list)
        else:
            for node in node.succeedNodes:
                new_list = []
                for node1 in list:
                    new_list.append(node1)
                self.combPath(node, new_list, allPaths)

    def maxFreq(self, FFPaths):
        maxF = 1111
        for path in FFPaths:
            T = 0
            for node in path:
                if path.index(node) == len(path) - 1:
                    T = T + node.setupTime
                else:
                    T = T + node.propDelay
            if 1/T < maxF:
                maxF = 1/T
        if maxF == 1111:
            return "No limit on the frequency"
        else :
            return maxF

    def holdTimeReq(self, FFPaths):
        nonSatPaths = []
        for path in FFPaths:
            T = 0
            for node in path:
                if path.index(node) == len(path) - 1:
                    if T < node.holdTime:
                        nonSatPaths.append(path)
                else:
                    T = T + node.propDelay
        for list in nonSatPaths:
            print(("", '\nWarning! Hold time condition is not satisfied in the following paths: ')[nonSatPaths.index(list) == 0])
            for node in list:
                print(node.nodeName + ",", end=' ')

    def findCombMax (self, gatePaths):
        maxDelay = 0
        for path in gatePaths:
            T = 0
            for node in path:
                T = T + node.propDelay
            if T > maxDelay:
                maxDelay = T
        if maxDelay == 0:
            return "0, No pure combinational paths, or ideal gates are assumed"
        else:
            return maxDelay

    def timingAnalyze(self):
        #Part 1, finding paths starting and ending with FFs
        allFFs = []
        FFPaths = []
        for node in self.allNodes:
            if node.nodeType == "FF":
                allFFs.append(node)
        for FF in allFFs:
            list = []
            self.checkFF(FF, list, FFPaths)
        #print the paths
        for list in FFPaths:
            print(("", 'FF paths: ')[FFPaths.index(list) == 0])
            for node in list:
                print(node.nodeName + ",", end=' ')
        print("\nMaximum frequency at which the circuit can operate: ")
        print (self.maxFreq(FFPaths))

        # Part 2, checking for hold time requirement
        self.holdTimeReq(FFPaths)

        #Part 3, finding path only with gates
        allGates = []
        gatePaths = []
        for node in self.allNodes:
            if node.nodeType == "GATE" and not node.proceedNodes:
                allGates.append(node)
        for gate in allGates:
            list = []
            self.combPath(gate, list, gatePaths)
        # print the paths
        print('')
        for list in gatePaths:
            print(("",'\nPure combinational paths: ') [gatePaths.index(list) == 0])
            for node in list:
                print(node.nodeName + ",", end=' ')
        print("\nThe largest delay caused by pure combinational path: ")
        print(self.findCombMax(gatePaths))





















