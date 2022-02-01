from node import Node
from netlist import Netlist

myCircuit = Netlist()

node1 = Node('FF1', 'FF', 0.5, 5, 1)
node2 = Node('FF2', 'FF', 0.5, 5, 1)
node3 = Node('AND1', 'GATE', 2)
#node4 = Node('FF3', 'FF', 0.5, 5, 1)
node5 = Node('AND2', 'GATE', 2)
node6 = Node('AND3', 'GATE', 2)
node7 = Node('AND4', 'GATE', 2)
node8 = Node('FF4', 'FF', 0.5, 5, 1)
node9 = Node('FF5', 'FF', 0.5, 5, 1)
node10 = Node('AND5', 'GATE', 2)
node11 = Node('AND6', 'GATE', 2)


myCircuit.addNode(node1, node3)
myCircuit.addNode(node2, node3, node5)
myCircuit.addNode(node10, node5)
myCircuit.addNode(node3, node6)
myCircuit.addNode(node5, node6, node7)
myCircuit.addNode(node6, node7, node8)
myCircuit.addNode(node7, node9, node11)
#myCircuit.addNode()

#check
for i in myCircuit.allNodes:
    print("\n" + i.nodeName)
    print("Proceeding nodes: ")
    for y in i.proceedNodes:
        print(y.nodeName, end = ' ')
    print("\nSucceeding nodes: ")
    for x in i.succeedNodes:
        print(x.nodeName, end = ' ')
    print('\n')

myCircuit.timingAnalyze()









