import math
from collections import defaultdict
from util.CoordinateUtil import CoordinateUtil
from util.Dijkstra import Dijkstra

class HmmProbabilities:
    def __init__(self, sigma, beta):
        self.sigma = sigma
        self.beta = beta
        

    def emission_probability(self, lat1, lon1, lat2, lon2, sigma):
        d = self.haversine_in_m(lat1, lon1, lat2, lon2)
        e = (1 / (math.sqrt(2 * math.pi) * sigma)) * math.exp(0.5 * ((d / sigma) ** 2))
        return e

  

    def return_id(self, a, b):
        combined = f"{a}-{b}"
        return hash(combined)

    def transmission_probability(self, graph, z1lat, z1lon, z2lat, z2lon, source, target, beta):
        dist = CoordinateUtil.haversine(z1lat, z1lon, z2lat, z2lon)
        dijkstra = Dijkstra()  
        dist2 = dijkstra.dijkstra(graph, source, target)  # Implement get_distance method
        transition_prob = (1 / beta) * math.exp(-abs(dist - dist2) / beta)
        return transition_prob

    def return_emission_probability(self, size, coordinate_size, candidates, coordinates):
        emission_prob = [[0 for _ in range(coordinate_size)] for _ in range(size)]
        outer_emission = 0
        for sublist in candidates:
            for s1 in sublist:
                for j in range(len(coordinates)):
                    if (
                        coordinates[j][0] == s1.latitude
                        and coordinates[j][1] == s1.longitude
                    ):
                        emission_prob[outer_emission][j] = s1.emission_prob
                outer_emission += 1
        return emission_prob

    def return_transmission_probability(self, size, candidates, graph):
        transmission_prob = [[0 for _ in range(size)] for _ in range(size)]
        outer = 0
        for sublist in candidates:
            for s1 in sublist:
                inner = 0
                for sublist2 in candidates:
                    for s2 in sublist2:
                        if int(s2.id) == (int(s1.id) + 1):
                            if (
                                s1.road_start == s2.road_start
                                and s1.road_end == s2.road_end
                            ):
                                index = -1
                                for i in range(len(graph[s1.road_start].out_edges)):
                                    if (
                                        self.return_vertex_num_from_edge(
                                            pg.edge[graph[s1.road_start].out_edges[i]],
                                            s1.road_start,
                                        )
                                        == s1.road_end
                                    ):
                                        index = graph[s1.road_start].out_edges[i]

                                if index != -1:
                                    transmission_prob[outer][inner] = pg.edge[index].weight
                                else:
                                    transmission_prob[outer][inner] = 0
                            else:
                                second = s2.road_start
                                if s1.road_start == s2.road_start:
                                    second = s2.road_end
                                transmission_prob[outer][inner] = self.transmission_probability(
                             
                                    s1.perpendicular_latitude,
                                    s1.perpendicular_longitude,
                                    s2.perpendicular_latitude,
                                    s2.perpendicular_longitude,
                                    s1.road_start,
                                    second,
                                    0.259442,
                                    graph,
                                
                                )
                        else:
                            transmission_prob[outer][inner] = 0
                        inner += 1
                outer += 1
        return transmission_prob