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

        if not self.Victim:
            randomMark = random.uniform(0, 1)
            if randomMark < pMP:
                packet.node = self.address
            return packet
        else:
            return packet



      
class Packet:
    node = ""

    def pPrint(self):
        for router in self.routerBuffer:
            print("\t" + str(router))

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

    nodeTable = []

    print(len(victimR.packetBuffer))

    for packet in victimR.packetBuffer:
        #print("Packet node: " + str(packet.node))
        if packet.node != '':
            checkResult = nodeTableCheck(packet,nodeTable)

            if checkResult != -1:
                #print("\tCheck Result: " + str(checkResult))
                #print(nodeTable[checkResult])
                nodeTable[checkResult][1] += 1
                #print(nodeTable)
            else:
                bufferTuple = [int(packet.node),0]

                nodeTable.append(bufferTuple)
                #print("Appened: " + str(bufferTuple))

    print("nodeTable:" + str(nodeTable))


    
        

def tupleCreation(packet,v,flag):
    tuple = []
    
    return tuple

    
    
def nodeTableCheck(packet,nt):

    if len(nt) == 0:
        return (-1)

    #print(len(nt))
    for i in range(len(nt)):
        if nt[i][0] == int(packet.node):
            return int(i)
    
    return -1



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

#Creating number range so attacker and victim cannot be the same 
numRange = list(range(1,21))
random.shuffle(numRange)

#Randomly select victim
victimRouter = numRange.pop()
routerList[victimRouter-1].Victim = True

#Randomly select attacker(s)
attackerRouter = numRange.pop()
routerList[attackerRouter-1].Attacker = True

#Defining the path between the two 
attackerVictimSP = nx.shortest_path(Network,source = attackerRouter,target = victimRouter)

addedTraffic = 5
    
print("attackerR: " + str(attackerRouter) + " victim router: " + str(victimRouter))
print("Shortest path between attacker and victim: "  + str(attackerVictimSP))


for i in range(simLength):

    #Select 5 random routers to send from that are not the attacker or the victim
    numRange = list(range(1,20))
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
    #packet.pPrint()

#print("Number of packets in victim buffer: " + str(len(routerList[victimRouter].packetBuffer)))

pathReconstruction(routerList[attackerRouter],routerList[victimRouter],len(attackerVictimSP))