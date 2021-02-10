"""
Christian Stoldal
CS 445 AS01
"""

import random
import numpy
import networkx as nx


#Packet marking probability
pMP = 0.2

#the attacker will send packets at a rate of X times the normal packet send rate
x = 10


class router:

    global pMP

    #IP address of the router initialized with 0
    address = 0

    #If true this router is an attacker
    Attacker = False
    #If true this router is a victim
    Victim = False
    #Packet buffer
    packetBuffer = []

    
    def __init__(self,addy):
        self.address = addy

    def __hash__(self):
        return self.address

    def packetMark(self, packet):
        randomMark = random.uniform(0, 1)
        if randomMark < pMP:
            packet.start = self.address
            packet.distance = 0
        else:
            if packet.distance == 0:
                packet.end = self.address
            packet.distance += 1
        return packet



      
class Packet:
    start = ""
    distance = 0
    end = ""

    def pPrint(self):
        print("\tPacket start: " + str(self.start))
        print("\tPacket distance: " + str(self.distance))
        print("\tPacket end: " + str(self.end))

def addEdges(n):
    fp = open('networkTop.txt','r')

    edgesList = []

    for row in fp:
        row = row.replace('\n','')
        edges = row.split(':')[1]
        edgesListBuffer = edges.split(',')
        edgesList.append(edgesListBuffer)
    
    for i in range(len(n)):
        for j in range(len(edgesList[i])):
            n.add_edge(i,int(edgesList[i][j]))
    
    return n

def sendPacket(rl,p,a,v):
    #print("Sending packets between router: " + str(a) + " and router: " + str(v))

    #Create packet
    packet = Packet()

    for router in p:
        #print("Current router traffic: " + str(router))
        packet = rl[router-1].packetMark(packet)

    rl[v-1].packetBuffer.append(packet)
    return packet


def pathReconstruction(attackR,victimR,d):

    packetsRecived = 0

    reconstructionTree = [victimR]
    
    for packet in attackR.packetBuffer:
        if packet.distance == 0:
            reconstructionTree.append(tupleCreation(packet,victimR,False))
        else:
            reconstructionTree.append(tupleCreation(packet,victimR,True))
        packetsRecived += 1
    
    #print(reconstructionTree)

    for i in range(2,len(reconstructionTree)):
        #print("The len of reconstruction tree is: " + str(len(reconstructionTree)))
        #print("i: " + str(i))
        #print(reconstructionTree[i-1])
        if reconstructionTree[i-1][2] != d:
            reconstructionTree.pop(i-1)
        if i >= len(reconstructionTree):
            break
    
    print("Nodes in reconstruction tree: " + str(len(reconstructionTree)))

    
        

def tupleCreation(packet,v,flag):
    tuple = []
    if flag:
        tuple.append(packet.start)
        tuple.append(packet.end)
        tuple.append(packet.distance)
    else:
        tuple.append(packet.start)
        tuple.append(v)
        tuple.append(0)
    return tuple

    
    




router1 = router(1)
router2 = router(2)
router3 = router(3)
router4 = router(4)
router5 = router(5)
router6 = router(6)
router7 = router(7)
router8 = router(8)
router9 = router(9)
router10 = router(10)
router11 = router(11)
router12 = router(12)
router13 = router(13)
router14 = router(14)
router15 = router(15)
router16 = router(16)
router17 = router(17)
router18 = router(18)
router19 = router(19)
router20 = router(20)              

routerList = [
    router1, 
    router2 ,
    router3,
    router4,
    router5,
    router6,
    router7,
    router8,
    router9,
    router10,
    router11,
    router12,
    router13,
    router14,
    router15,
    router16,
    router17,
    router18,
    router19,
    router20              
]


#Create graph
Network = nx.Graph()

initialNodes = []
#Creating network nodes
for i in range(len(routerList)):
    Network.add_node(routerList[i])
    initialNodes.append(routerList[i])
    

 

#Give each node a random position
NodePos = nx.spring_layout(Network)

#Random number for edge generation
numberOfEdge = random.randint(20,25)

#print(len(network))
Network = addEdges(Network)


simLength = 100


#Randomly select victim
victimRouter = random.randint(1,20)
routerList[victimRouter-1].Victim = True

#Randomly select attacker(s)
attackerRouter = random.randint(1,20)
routerList[attackerRouter-1].Attacker = True

#Defining the path between the two 
attackerVictimSP = nx.shortest_path(Network,source = attackerRouter,target = victimRouter)

addedTraffic = 5
    
for i in range(simLength):

    #Select 5 random routers to send from that are not the attacker or the victim
    numRange = list(range(1,21))
    #print("attackerR: " + str(attackerRouter) + " victim router: " + str(victimRouter))
    numRange.remove(attackerRouter)
    numRange.remove(victimRouter)
    random.shuffle(numRange)

    addedRouters = []

    for i in range(addedTraffic):
        addedRouters.append(numRange.pop())
    
    #Standard traffic
    for i in range(len(addedRouters)):
        standardTrafficSP = nx.shortest_path(Network,source = addedRouters[i],target = victimRouter)
        sendPacket(routerList,standardTrafficSP,addedRouters[i],victimRouter)

    #Attacker traffic
    for i in range (x):
        sendPacket(routerList,attackerVictimSP,victimRouter,attackerRouter)

#print(routerList[victimRouter].packetBuffer)

#for packet in routerList[victimRouter].packetBuffer:
#    packet.pPrint()

pathReconstruction(routerList[attackerRouter],routerList[victimRouter],len(attackerVictimSP))