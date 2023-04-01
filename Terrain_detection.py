import cv2
from realsense_depth import *
import matplotlib.pyplot as plt
from grid_of_pixels import GridOfPixels
from data_smoother import DataSmoother
from data_cluster_1 import DBSCANClusterer

clusterer = DBSCANClusterer(eps=5, min_samples=10)
data_smoother = DataSmoother(window_size=50)

def get_instant_frame():
    dc = DepthCamera()
    ret, depth_frame, color_frame = dc.get_frame()
    return ret, depth_frame, color_frame

def create_grid_coordinates(width, height, grid_size):
    grid = GridOfPixels(width, height, grid_size)
    pixel_coordinates = grid.create()
    return pixel_coordinates
    
def get_pixel_depths(color_frame, depth_frame, pixel_coordinates):
    pixel_depths = []
    for coordinate in pixel_coordinates:
        point = (coordinate[0],coordinate[1])
        cv2.circle(color_frame, point, 4, (0,0,255))
        
        pixel_depth = (depth_frame[coordinate[1], coordinate[0]])
        pixel_depths.append(pixel_depth)
    return pixel_depths
    
if __name__ == "__main__":

    ret,depth_frame, color_frame = get_instant_frame()
    pixel_coordinates = create_grid_coordinates(width = 640, height = 480, grid_size = 50)
    pixel_depths = get_pixel_depths(color_frame, depth_frame, pixel_coordinates)
    pixel_depths = [i for i in pixel_depths if i != 0]
    smoothed_data = data_smoother.smooth(pixel_depths)
    fig1 = plt.figure()
    plt.imshow(cv2.cvtColor(color_frame, cv2.COLOR_BGR2RGB))
    fig2 = plt.figure()
    plt.ylim(300,2000)
    plt.plot(smoothed_data)
    clusterer.fit(pixel_depths)
    clusterer.plot()
    plt.show()

    # plt.imshow('color_frame', color_frame, cv2.COLOR_BGR2RGB)


