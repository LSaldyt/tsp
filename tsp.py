import numpy as np

class Problem:
    def __init__(self, n_cities, size=10):
        ''' Generate a TSP instance on an nxn grid with m cities '''
        self.n_cities = n_cities
        self.size     = size
        self.points = np.random.uniform(0, size, (self.n_cities, 2))
        self.distance_matrix = self.make_distance_matrix(self.points)

    def make_distance_matrix(self, points):
        distance_matrix = np.zeros((self.n_cities, self.n_cities))
        normalize = np.hypot(self.size, self.size)
        for i in range(self.n_cities):
            for j in range(self.n_cities):
                distance_matrix[i, j] = (np.hypot(points[i][0] - points[j][0],
                                                  points[i][1] - points[j][1])
                                         / normalize)
        return distance_matrix
