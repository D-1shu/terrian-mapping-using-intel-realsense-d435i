import cv2
from realsense_depth import *
import matplotlib.pyplot as plt
from grid_of_pixels import GridOfPixels
from data_smoother import DataSmoother
from data_cluster_1 import DBSCANClusterer

dc = DepthCamera()

ret, depth_frame, color_frame = dc.get_frame()

width = 640
height = 480
grid_size = 50

grid = GridOfPixels(width, height, grid_size)
pixel_coordinates = grid.create()
pixel_depths = []
for coordinate in pixel_coordinates:
    point = (coordinate[0],coordinate[1])
    cv2.circle(color_frame, point, 4, (0,0,255))
    
    pixel_depth = (depth_frame[coordinate[1], coordinate[0]])
    pixel_depths.append(pixel_depth)


# cv2.imshow('color_frame', color_frame)

pixel_depths = [i for i in pixel_depths if i != 0]
clusterer = DBSCANClusterer(eps=10, min_samples=10)
data_smoother = DataSmoother(window_size=50)
smoothed_data = data_smoother.smooth(pixel_depths)
fig, ax = plt.subplots(nrows=1, ncols=2)
ax[0].imshow(cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB))
ax[1].set_ylim(300,2000)
ax[1].plot(smoothed_data)
clusterer.fit(pixel_depths)
clusterer.plot()
plt.show()
