from animation import frame as f
from animation import layer as l
from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt

class XSheetTable(QMainWindow):
    def __init__(self, layers):
        super().__init__()

        self.layers = layers

        # Create a central widget and layout for the table
        central_widget = QWidget(self)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        numColumns = 1 + 2 * len(layers)
        numRows = max([len(layer.frames) for layer in layers])

        self.tableWidget = QTableWidget(numRows + 1, numColumns)
        layout.addWidget(self.tableWidget)

        self.populate_table()

    def populate_table(self):
        numColumns = 1 + 2 * len(self.layers)
        numRows = max([len(layer.frames) for layer in self.layers])

        self.tableWidget.setRowCount(numRows + 1)  # +1 for the buttons row
        self.tableWidget.setColumnCount(numColumns)

        headers = ["Frame"] + [f"{layer.name} Key Type" for layer in self.layers] + [f"{layer.name} Ease Type" for layer in self.layers]
        self.tableWidget.setHorizontalHeaderLabels(headers)

        for row in range(numRows):
            for col in range(numColumns):
                if col == 0:
                    # Fill in the frame numbers in the first column
                    if row < len(self.layers[0].frames):
                        frameNumber = self.layers[0].frames[row].frameNumber
                        item = QTableWidgetItem(str(frameNumber))
                        item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
                        item.setFlags(item.flags() & ~Qt.ItemFlag.ItemIsEditable)  # Make the item not editable
                        self.tableWidget.setItem(row, col, item)
                elif col % 2 == 1:
                    # Fill in the key types in odd-numbered columns
                    layerIndex = (col - 1) // 2
                    if row < len(self.layers[layerIndex].frames):
                        keyType = self.layers[layerIndex].frames[row].keyType or ""
                        combo = QComboBox()
                        combo.addItems(f.c.KEYTYPES)
                        combo.setCurrentText(keyType)
                        combo.currentTextChanged.connect(lambda text, layerIndex=layerIndex: setattr(self.layers[layerIndex].frames[row], 'keyType', text))
                        self.tableWidget.setCellWidget(row, col, combo)
                else:
                    # Fill in the ease types in even-numbered columns
                    layerIndex = (col - 2) // 2
                    if row < len(self.layers[layerIndex].frames):
                        easeType = self.layers[layerIndex].frames[row].easeType or ""
                        combo = QComboBox()  # Use the custom QComboBox
                        combo.addItems(f.c.EASETYPES)
                        combo.setCurrentText(easeType)
                        combo.currentTextChanged.connect(lambda text, layerIndex=layerIndex: setattr(self.layers[layerIndex].frames[row], 'easeType', text))
                        self.tableWidget.setCellWidget(row, col, combo)

        # Add buttons row
        for col, layer in enumerate(self.layers, start=1):
            button = QPushButton("+")
            button.clicked.connect(lambda clicked_layer=layer: self.add_new_frame(clicked_layer))
            self.tableWidget.setCellWidget(numRows, col if col % 2 == 1 else col + 1, button)

    def add_new_frame(self, layer):
        new_frame_number = len(layer.frames) + 1
        new_frame = f.Frame(new_frame_number, "key")
        layer.frames.append(new_frame)

        self.populate_table()



if __name__ == "__main__":
    # Create some sample data
    layer1 = l.Layer("Layer 1",[])
    layer1.frames.append(f.Frame(1, "key"))
    layer1.frames.append(f.Frame(2, "breakdown", "easeOut"))
    layer1.frames.append(f.Frame(3, "anticipation", "easeIn"))
    layer2 = l.Layer("Layer 2",[])
    layer2.frames.append(f.Frame(1, "key", "easeOut"))
    layer2.frames.append(f.Frame(2, "breakdown"))
    layers = [layer1, layer2]

    # Create the application and main window
    app = QApplication([])
    window = QMainWindow()
    window.setWindowTitle("XSheet Table")

    # Create the table widget and add it to the main window
    tableWidget = XSheetTable(layers)
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