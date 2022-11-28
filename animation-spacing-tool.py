class frame:
    def __init__(self, number, keytype, easetype = None, easeVal = None, motionID = None, division = None):
        self.number = number
        self.keytype = keytype
        self.motionID = motionID
        # for keys, extreme, anticipation, overshoot and breakdowns.
        self.easetype = easetype  # defines distribution of inbetween spacings from one to another.
        # for inbetweens
        self.easeVal = easeVal # percentage of easing (for inbetweens only)
        self.division = division # the number of the current division between keys

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