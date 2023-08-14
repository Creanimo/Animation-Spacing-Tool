from animation import frame as f
from animation import layer as l
from xsheet import table as uix

if __name__ == "__main__":
    # Create some sample data
    layer1 = l.Layer("Layer 1",[])
    layer1.frames.append(f.Frame(1, "key", "easeOut"))
    layer1.frames.append(f.Frame(7, "breakdown", "easeIn"))
    layer1.frames.append(f.Frame(11, "anticipation", "easeOut"))
    layer1.evaluateMotion()
    layer2 = l.Layer("Layer 2",[])
    layer2.frames.append(f.Frame(1, "key", "easeOut"))
    layer2.frames.append(f.Frame(13, "breakdown"))
    layer2.evaluateMotion()
    layers = [layer1, layer2]

    # Create the application and main window
    app = uix.QApplication([])
    window = uix.QMainWindow()
    window.setWindowTitle("XSheet Table")

    # Create the table widget and add it to the main window
    tableWidget = uix.XSheetTable(layers)
    window.setCentralWidget(tableWidget)

    # Show the main window and start the event loop
    window.show()
    app.exec()

   



"""
def main():
    frameKey = f.Frame(frameNumber=1, keyType="key", easeType="easeOut", steps=2)
    frameBreakdown = f.Frame(frameNumber=11, keyType="breakdown", easeType="easeIn", steps=2)
    frameInbetween = f.Frame(frameNumber=13, keyType="inbetween")
    frameKey2 = f.Frame(frameNumber=19, keyType="key", easeType="easeOut", steps = 2)
    frameBreakdown2 = f.Frame(frameNumber=25, keyType="breakdown", easeType="easeIn")
    L = l.Layer(name = "Layer1", frames = [frameKey, frameKey2, frameBreakdown2, frameBreakdown, frameInbetween])
    L.evaluateMotion()
    # print(l.calculateEaseInSpacings(5))
    # print(l.calculateEaseOutSpacings(7))
    # print(l.calculateLinearSpacings(5))
    # jsonOutput = L.convertToJSON()
    # with open("layer.json", "w") as json_file:
    #    json_file.write(jsonOutput)

if __name__ == '__main__':
    main()



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