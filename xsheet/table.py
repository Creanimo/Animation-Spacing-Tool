from PyQt6.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QComboBox, QPushButton, QVBoxLayout, QWidget
from PyQt6.QtCore import Qt
from animation import frame as f

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