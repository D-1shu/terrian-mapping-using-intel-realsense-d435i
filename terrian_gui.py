import sys
import numpy as np
import cv2
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from PyQt5 import uic
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from realsense_depth import *
import matplotlib.pyplot as plt
from grid_of_pixels import GridOfPixels
from data_smoother import DataSmoother
from data_cluster_1 import DBSCANClusterer
from frame_processor import FrameProcessor

#global variables
ret = False
depth_frame = None
color_frame = None
canvas1 = None
canvas2 = None
canvas3 = None
canvas4 = None
canvas5 = None
pixel_coordinates = None
pixel_depths = None
smoothed_data = None

#objects
dc = DepthCamera()
clusterer = DBSCANClusterer(eps=2, min_samples=5)
data_smoother = DataSmoother(window_size=50)
depth_color_frame = FrameProcessor()
def get_instant_frame():
    global ret
    global depth_frame
    global color_frame
    global canvas1
    ret, depth_frame, color_frame = dc.get_frame()
    figure1 = Figure()
    canvas1 = FigureCanvas(figure1)
    ax1 = figure1.add_subplot(111)
    ax1.set_title("Captured Image")
    ax1.imshow(cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB))
    layout1.addWidget(canvas1,0,0)
    return ret, depth_frame, color_frame

def clear():
    global canvas1
    global canvas2
    global canvas3
    global canvas4

    layout1.removeWidget(canvas1)
    canvas1.deleteLater()

    #if(canvas2!= None):
    layout1.removeWidget(canvas2)
    canvas2.deleteLater()

    #if(canvas3!= None):
    layout1.removeWidget(canvas3)
    canvas3.deleteLater()

    #if(canvas4!=None):
    layout1.removeWidget(canvas4)
    canvas4.deleteLater()

    layout2.removeWidget(canvas5)
    canvas5.deleteLater()



def create_grid_coordinates(width, height, grid_size):
    global pixel_coordinates
    grid = GridOfPixels(width, height, grid_size)
    pixel_coordinates = grid.create()
    return pixel_coordinates
    
def get_pixel_depths(color_frame, depth_frame, pixel_coordinates):
    global pixel_depths
    pixel_depths = []
    for coordinate in pixel_coordinates:
        point = (coordinate[0],coordinate[1])
        cv2.circle(color_frame, point, 4, (0,0,255))  
        pixel_depth = (depth_frame[coordinate[1], coordinate[0]])
        pixel_depths.append(pixel_depth)
    return pixel_depths

def process_data():
    global canvas2
    global canvas3
    global canvas4
    global canvas5
    global ret
    global color_frame
    global depth_frame
    global pixel_coordinates
    global pixel_depths
    global smoothed_data
    
    pixel_coordinates = create_grid_coordinates(width = 640, height = 480, grid_size = 50)
    pixel_depths = get_pixel_depths(color_frame, depth_frame, pixel_coordinates)
    pixel_depths = [i for i in pixel_depths if i != 0]
    smoothed_data = data_smoother.smooth(pixel_depths)

    figure2 = Figure()
    canvas2 = FigureCanvas(figure2)
    ax2 = figure2.add_subplot(111)
    ax2.set_title("Depth Pixels Selected")
    ax2.imshow(cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB))
    layout1.addWidget(canvas2,0,1)

    figure3 = Figure()
    canvas3 = FigureCanvas(figure3)
    ax3 = figure3.add_subplot(111)
    ax3.set_ylim(300,2000)
    ax3.set_title("Depth Profile")
    ax3.set_xlabel("Flattened Pixels")
    ax3.set_ylabel("Height in mm")
    ax3.plot(smoothed_data)
    layout1.addWidget(canvas3,1,0)

    clusterer.fit(pixel_depths)
    canvas4 = FigureCanvas(clusterer.plot())
    layout1.addWidget(canvas4,1,1)

    canvas5 = FigureCanvas(depth_color_frame.process_frames(depth_frame=depth_frame, color_frame=color_frame))
    layout2.addWidget(canvas5)


def halt():
    dc.release()

# create the application instance
app = QApplication(sys.argv)

# load the UI file
ui_file = "test_matlab.ui"
ui = uic.loadUi(ui_file)
ui.capture.clicked.connect(get_instant_frame)
ui.halt.clicked.connect(halt)
ui.clear.clicked.connect(clear)
ui.process.clicked.connect(process_data)

# get a reference to the first layout created in Qt Designer
layout1 = ui.gridLayout
layout2 = ui.gridLayout_3

# set the window titlecall.button1.clicked.connect(loginf)
ui.setWindowTitle("Matplotlib in PyQt5")

# show the main window
ui.show()

# run the application event loop
sys.exit(app.exec_())
