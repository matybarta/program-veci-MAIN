import time

class Toping:

    outsideTemp = 10
    toping = False

    def __init__(self, name, capacity, startTemp, startHeat, stopHeat):
        self.name = name
        self.capacity = capacity
        self.startTemp = startTemp
        self.startHeat = startHeat
        self.stopHeat = stopHeat

        self.Heat = True
        self.actualTemp = startTemp
        self.startTime = time.time()
        print(f"Topeni {self.name} je ZAPNUTO a má {self.actualTemp}")


    @staticmethod
    def boolToSwitch(toSwitch):
        if toSwitch:
            return "ZAPNUTO"
        else:
            return "VYPNUTO"
    
    @classmethod
    def setOutsideTemp(cls, temp):
        cls.outsideTemp = temp

    @classmethod
    def startToping(cls):
        cls.toping = True

    @classmethod
    def stopToping(cls):
        cls.toping = False

    def regulateHeating(self):
        myTime = time.time() - self.startTime
        if self.Heat:
            self.actualTemp = self.startTime + myTime * self.capacity
        else:
            self.actualTemp = self.startTime - myTime * self.capacity
        print(f"Topeni {self.name} je {self.boolToSwitch(self.Heat)} a má {self.actualTemp}")
        



Toping.setOutsideTemp(10)
Toping.startToping()

heating1 = Toping("obývák", 0.7, 10, 7 ,10)


while True:
    heating1.regulateHeating()
    time.sleep(1)
