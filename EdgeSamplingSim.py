import random
import networkx as nx


#Packet marking probability
pMP = 0


class router:

    global pMP

    #IP address of the router initialized with 0
    address = 0

    #If true this router is an attacker
    Attacker = False
    #If true this router is a victim
    Victim = False

    
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



      
class packet:
    start = ""
    distance = 0
    end = ""

def addEdges(n):
    fp = open('networkTop.txt','r')

    edgesList = []

    for row in fp:
        row = row.replace('\n','')
        edges = row.split(':')[1]
        edgesListBuffer = edges.split(',')
        edgesList.append(edgesListBuffer)
    
    for i in range(len(Network)):
        for j in range(len(edgesList[i])):
            Network.add_edge(i,int(edgesList[i][j]))
    
    return Network

def sendPackets(p,a,v):
    print("Sending packets between router: " + str(a) + " and router: " + str(v))
    
    




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

    
for i in range(simLength):
    sendPackets(attackerVictimSP,victimRouter,attackerRouter)
