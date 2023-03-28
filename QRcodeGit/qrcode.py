import numpy as np


class QRCode:
    def __init__(self, data, rect, polygon, quality, orientation):
        self.data = data
        self.rect = rect
        self.polygon = polygon
        self.quality = quality
        self.orientation = orientation

    def get_data(self):
        return self.data.decode('utf-8')

    def get_polygon(self):
        points = np.array([self.polygon], np.int32)
        return points.reshape((-1, 1, 2))







