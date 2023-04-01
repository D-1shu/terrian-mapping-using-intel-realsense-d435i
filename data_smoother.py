import numpy as np

class DataSmoother:
    def __init__(self, window_size=50):
        self.window_size = window_size

    def smooth(self, data):
        # Compute the average after every window_size data points
        averages = []
        for i in range(0, len(data), self.window_size):
            avg = np.mean(data[i:i+self.window_size])
            averages.extend([avg]*self.window_size)

        # Replace the original data points with the averages
        smooth_data = np.array(averages)
        return smooth_data
