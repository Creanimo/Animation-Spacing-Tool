from animation import frame as f
from animation import layer as l


def main():
    frameKey = f.Frame(frameNumber=1, keyType="key", easeType="easeOut")
    frameBreakdown = f.Frame(frameNumber=9, keyType="breakdown", easeType="easeIn")
    frameInbetween = f.Frame(frameNumber=11, keyType="inbetween")
    frameKey2 = f.Frame(frameNumber=17, keyType="key", easeType="easeOut")
    L = l.Layer(name = "Layer1", frames = [frameKey, frameKey2, frameBreakdown, frameInbetween])
    # L.evaluateMotion()
    print(l.calculateEaseInSpacings(5))
    print(l.calculateEaseOutSpacings(5))
    print(l.calculateLinearSpacings(5))
    jsonOutput = L.convertToJSON()
    with open("layer.json", "w") as json_file:
        json_file.write(jsonOutput)

if __name__ == '__main__':
    main()


"""
class layer:
    def __init__(self, name, frames):
        self.name = name
        self.frames = frames

    def evaluateMotion(self):
        sorted(self.frames, key=lambda x: x.number)
        i = 0
        motionCount = 0
        # assign motion IDs and divider count
        while i<=len(self.frames)-1:
            if self.frames[i].keytype in ["key","extreme","anticipation","overshoot","breakdown"]:
                motionCount += 1
                dividerCount = 0
            if self.frames[i].keytype in ["inbetween"]:
                dividerCount +=1
                self.frames[i].division = dividerCount
            self.frames[i].motionID = motionCount
            i += 1
            continue
        highestMotionCount = motionCount
        # write ease percentage to divisions
        divisionPercentage = 100
        i = 0
        motionCount = 1
        while i<=len(self.frames)-1:
            if self.frames[i].motionID == motionCount and self.frames[i].keytype == "inbetween":
                # works for easeIn... for easeOut try next: count up until you find division None, then loop again through the just counted (backwards?)
                divisionPercentage = divisionPercentage / 2
                self.frames[i].easeVal = divisionPercentage
                i += 1
                continue
            if self.frames[i].motionID > motionCount:
                i += 1
                divisionPercentage = 100
                motionCount +=1
                continue
            i +=1
        return


SetOfFrames = [frame(1,"key","easeOut"), frame(3,"inbetween"), frame(5,"inbetween"), frame(7,"inbetween"), frame(9, "breakdown","easeIn"), frame(11,"inbetween"), frame(13,"key","easeOut")]
Layer1 = layer("Arm",SetOfFrames)


print(SetOfFrames[2].keytype)
Layer1.evaluateMotion()
print(Layer1.frames[3].division)
print("Result")
for i in Layer1.frames:
    if i.easeVal != None:
        print(i.easeVal)
    else:
        print(i.keytype)
"""
