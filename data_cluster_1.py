import numpy as np
from sklearn.cluster import DBSCAN
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
class DBSCANClusterer:
    def __init__(self, eps=0.5, min_samples=5):
        self.eps = eps
        self.min_samples = min_samples
        self.dbscan = DBSCAN(eps=self.eps, min_samples=self.min_samples)
        
    def fit(self, data):
        self.data = np.array(data).reshape(-1, 1)
        self.dbscan.fit(self.data)
        self.labels = self.dbscan.labels_
        self.n_clusters = len(set(self.labels)) - (1 if -1 in self.labels else 0)
        self.noise_points = np.sum(self.labels == -1)
        
    def plot(self):
        figure = Figure()
        ax = figure.add_subplot(111)
        colors = plt.cm.nipy_spectral(np.linspace(0, 1, len(set(self.labels))))
        count = 1
        for i, color in zip(range(len(set(self.labels))), colors):
            indices = np.where(self.labels == i)[0]
            ax.scatter(indices, self.data[indices], color=color, label="Height %d" % i)
            count = count+ int(i)
        self.no_of_heights = count

        ax.set_xlabel("Index")
        ax.set_ylabel("Data Value")
        ax.legend()
        return figure
        # plt.show()