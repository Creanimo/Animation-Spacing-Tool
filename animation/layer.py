import constants as c
import frame as f

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

        
def convertFloatToInt(number):
    if number == int(number):
        return int(number)
    else:
        return number

def main():
    frameKey = f.Frame(frameNumber=1, keyType="key")
    frameBreakdown = f.Frame(frameNumber=9, keyType="breakdown")
    frameInbetween = f.Frame(frameNumber=11, keyType="inbetween")
    frameKey2 = f.Frame(frameNumber=17, keyType="key")
    L = Layer(name = "Layer 1", frames = [frameKey, frameKey2, frameBreakdown, frameInbetween])
    L.evaluateMotion()

if __name__ == '__main__':
    main()