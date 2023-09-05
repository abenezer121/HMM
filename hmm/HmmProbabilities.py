import math
from collections import defaultdict
from util.CoordinateUtil import CoordinateUtil
from util.Dijkstra import Dijkstra
import numpy as np


class HmmProbabilities:
    def __init__(self, sigma, beta):
        self.sigma = sigma
        self.beta = beta
        self.coordinateUtil = CoordinateUtil()
        


    def emission_probability(self, lat1, lon1, lat2, lon2):
        d = self.coordinateUtil.haversine(lat1, lon1, lat2, lon2)/1000
        e = (1 / (math.sqrt(2 * math.pi) * self.sigma)) * math.exp(0.5 * ((d / self.sigma) ** 2))
        return e

  




    def return_emission_probability(self, size, coordinate_size, candidates, coordinates):
        emission_prob = [[0 for _ in range(coordinate_size)] for _ in range(size)]
        outer_emission = 0
        for sublist in candidates:
            for s1 in sublist:
                for j in range(len(coordinates)):
                    if (
                        coordinates[j][0] == s1.get_latitude()
                        and coordinates[j][1] == s1.get_longitude()
                    ):
                        emission_prob[outer_emission][j] = s1.get_emission_probability()
                outer_emission += 1
        return emission_prob
    


    def transmission_probability(self, z1lat, z1lon, z2lat, z2lon, source, target,graph):
        dist = self.coordinateUtil.haversine(z1lat, z1lon, z2lat, z2lon)
        dijkstra = Dijkstra()  
        dist2 = dijkstra.dijkstra(graph, source, target)  # Implement get_distance method
 
        transition_prob = (1 / self.beta) * np.exp(-abs(dist - dist2) / self.beta)
        return transition_prob

    def return_transmission_probability(self, size, candidates, graph):
        transmission_prob = [[0 for _ in range(size)] for _ in range(size)]
        outer = 0
        for sublist in candidates:
            for s1 in sublist:
                inner = 0
                for sublist2 in candidates:
                    for s2 in sublist2:
                        if int(s2.get_id()) == (int(s1.get_id()) + 1):
                                                      
                                transmission_prob[outer][inner] = self.transmission_probability(
                             
                                    s1.get_latitude(),
                                    s1.get_longitude(),
                                    s2.get_latitude(),
                                    s2.get_longitude(),
                                    s1.get_nodeid(),
                                    s2.get_nodeid(),
                                    graph,
                                
                                )
                        else:
                            transmission_prob[outer][inner] = 0
                        inner += 1
                outer += 1
        return transmission_prob


   