import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

# create the application instance
app = QApplication(sys.argv)

# load the UI file
ui_file = "test_matlab.ui"
ui = uic.loadUi(ui_file)

# get a reference to the first layout created in Qt Designer
layout1 = ui.gridLayout

# create a Matplotlib figure and add a plot
figure1 = Figure()
canvas1 = FigureCanvas(figure1)
ax1 = figure1.add_subplot(111)
x = np.linspace(0, 10, 100)
y = np.sin(x)
ax1.plot(x, y)

# add the first canvas to the first layout
layout1.addWidget(canvas1)

# create a second Matplotlib figure and add a plot
figure2 = Figure()
canvas2 = FigureCanvas(figure2)
ax2 = figure2.add_subplot(111)
x = np.linspace(0, 10, 100)
y = np.cos(x)
ax2.plot(x, y)

# add the second canvas to the second layout
layout1.addWidget(canvas2)


# create a second Matplotlib figure and add a plot
figure3 = Figure()
canvas3 = FigureCanvas(figure3)
ax3 = figure3.add_subplot(111)
x = np.linspace(0, 10, 100)
y = np.tan(x)
ax3.plot(x, y)

# add the second canvas to the second layout
layout1.addWidget(canvas3)


# set the window title
ui.setWindowTitle("Matplotlib in PyQt5")

# show the main window
ui.show()

# run the application event loop
sys.exit(app.exec_())
