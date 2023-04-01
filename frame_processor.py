import numpy as np
import cv2
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
class FrameProcessor:
    def __init__(self):
        pass
        
    def process_frames(self, depth_frame, color_frame):
        # Convert images to numpy arrays
        # depth_image = np.asanyarray(depth_frame.get_data())
        # color_image = np.asanyarray(color_frame.get_data())

        depth_image = depth_frame
        color_image = color_frame

        # Apply colormap on depth image (image must be converted to 8-bit per pixel first)
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.2), cv2.COLORMAP_JET)

        depth_colormap_dim = depth_colormap.shape
        color_colormap_dim = color_image.shape

        # If depth and color resolutions are different, resize color image to match depth image for display
        # if depth_colormap_dim != color_colormap_dim:
        #     resized_color_image = cv2.resize(color_image, dsize=(depth_colormap_dim[1], depth_colormap_dim[0]), interpolation=cv2.INTER_AREA)
        #     images = np.hstack((resized_color_image, depth_colormap))
        # else:
        #     images = np.hstack((color_image, depth_colormap))

        # # Convert the image to RGB format for display with matplotlib
        image = cv2.cvtColor(depth_colormap, cv2.COLOR_BGR2RGB)

        # Create a figure and display the images
        figure = Figure()
        ax = figure.add_subplot(111)
        depth_color_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        ax.imshow(depth_color_image)
        ax.set_title("Topography of Terrian")
        ax.axis('off')

        # Return the figure object
        return figure