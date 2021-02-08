

class router:
    address = 0
    
    def __init__(self,addy):
        self.address = addy

    def __hash__(self):
        return self.address

    def packetMark(self, packet):
        print("Test")


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


network = {
    router1 : {},
    router2 : {},
    router3 : {},
    router4 : {}, 
    router5 : {},
    router6 : {}, 
    router7 : {}, 
    router8 : {}, 
    router9 : {}, 
    router10 : {}, 
    router11 : {}, 
    router12 : {},
    router13 : {}, 
    router14 : {}, 
    router15 : {}, 
    router16 : {}, 
    router17 : {}, 
    router18 : {}, 
    router19 : {}, 
    router20 : {} 
}

