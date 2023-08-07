from animation import constants as c
from animation import frame as f

class Layer:
    def __init__(self, name, frames):
        self._validateName(name)
        self._validateFrames(frames)

        self.name = name
        self.frames = frames

    def _validateName(self, name):
        if not isinstance(name, str):
            raise TypeError("Layer name must be a string.")
        
    def _validateFrames(self, frames):
        if not isinstance(frames, list):
            raise TypeError("frames must be a list of Frame objects.")
        for i in frames:
            if not isinstance(i, f.Frame):
                raise TypeError("frame list must only hold Frame objects.")
            
    def sortFrames(self):
        toSort = self.frames
        newOrder = sorted(toSort, key=lambda x: x.frameNumber)
        self.frames = newOrder
            
    def evaluateMotion(self):
        self.sortFrames()

        # making an index of frames by frame number
        frameIndex = {}
        for i in self.frames:
            frameIndex[i.frameNumber] = i

        currentFrame = 1
        currentStep = 2
        currentSpacingCount = 0
        # getting the highest frame number
        lastFrame = self.frames[-1].frameNumber
        while currentFrame <= lastFrame:
            if (currentFrame in frameIndex.keys()) and (frameIndex[currentFrame].keyType not in ("inbetween", "hold")):
                print(currentFrame)
            elif currentFrame not in frameIndex.keys():
                if (currentFrame - 1) % currentStep == 0:
                    self.frames.append(f.Frame(keyType="inbetween", frameNumber=currentFrame))
                else:
                    self.frames.append(f.Frame(keyType="hold", frameNumber=currentFrame))
            currentFrame += 1

        self.sortFrames()
        for i in self.frames:
            print(i.frameNumber, i.keyType)

def assignSpacingsEaseOut(numOfInbetweens):
    easePercentageIncrement = 1.0 / (2 ** numOfInbetweens)
    currentEasePercentage = 1.0
    easePercentageValues = []

    for i in range(1, numOfInbetweens + 1):
        currentEasePercentage -= easePercentageIncrement
        easePercentageValues.append(currentEasePercentage)

    print(easePercentageValues)
    return easePercentageValues

def calculateEaseOutSpacings(totalDivisions):
    i=1
    currentPercentage=1.0
    easePercentages=[]
    while i<=totalDivisions:
        currentPercentage = currentPercentage/2
        easePercentages.append(currentPercentage)
        i+=1
    easePercentages.reverse()
    return easePercentages

def calculateEaseInSpacings(totalDivisions):
    i=2
    easePercentages=[0.5]
    basePercentage=0.5
    while i<=totalDivisions:
        basePercentage=basePercentage/2
        currentPercentage = easePercentages[i-2] + basePercentage
        easePercentages.append(currentPercentage)
        i+=1
    return easePercentages

def calculateLinearSpacings(totalDivisions):
    basePercentage = 1.0
    basePercentage = basePercentage / (totalDivisions + 1)
    easePercentages = [basePercentage]
    currentPercentage = basePercentage
    i=2
    while i<= totalDivisions:
        currentPercentage += basePercentage
        easePercentages.append(currentPercentage)
        i+=1
    return easePercentages

        
def convertFloatToInt(number):
    if number == int(number):
        return int(number)
    else:
        return number

