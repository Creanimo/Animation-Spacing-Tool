import json
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
            
    def evaluateMotion(self, startFrame=1):
        self.sortFrames()
        # making an index of frames by frame number
        frameIndex = {}
        for i in self.frames:
            frameIndex[i.frameNumber] = i

        # getting the highest frame number
        lastFrame = self.frames[-1].frameNumber

        current_major_keyframe = None
        for frame in self.frames:
            if frame.keyType in c.KEYTYPES_MOTIONEND:
                if current_major_keyframe is None:
                    current_major_keyframe = frame
                else:
                    spacing_count = (frame.frameNumber - current_major_keyframe.frameNumber)  // current_major_keyframe.steps - 1
                    current_major_keyframe.spacingCount = spacing_count
                    current_major_keyframe = frame


        
        """
        currentFrame = 1
        currentStep = 2
        currentSpacingCount = 0
        
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
        """
        
        for i in self.frames:
            print(i.frameNumber, i.keyType, i.spacingCount)

    def convertToJSON(self):
        frames_dict = {}
        for frame in self.frames:
            frame_number = frame.frameNumber
            frame_dict = {
                "keyType": frame.keyType,
                "easeType": frame.easeType,
                "easeVal": frame.easeVal,
                "motionID": frame.motionID,
                "spacingCount": frame.spacingCount,
                "steps": frame.steps
            }
            frames_dict[frame_number] = frame_dict

        layer_dict = {
            "name": self.name,
            "frames": frames_dict
        }

        return json.dumps(layer_dict, indent=4)
    
def JSONtoLayer(jsonString):
    layer_data = json.loads(jsonString)

    name = layer_data.get("name")
    frames_dict = layer_data.get("frames", {})

    frames = []
    for frame_number, frame_dict in frames_dict.items():
        frame = Frame(
            frameNumber=int(frame_number),
            keyType=frame_dict.get("keyType"),
            easeType=frame_dict.get("easeType"),
            easeVal=frame_dict.get("easeVal"),
            motionID=frame_dict.get("motionID"),
            spacingCount=frame_dict.get("spacingCount"),
            steps=frame_dict.get("steps", 1)
        )
        frames.append(frame)

    layer = Layer(name, frames)
    return layer


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

