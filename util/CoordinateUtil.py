import math
import heapq

class CoordinateUtil:
        def haversine(self,lat1, lon1, lat2, lon2):
            
            earth_radius = 6371000.0 # Radius of the Earth in meters
            lat1, lon1, lat2, lon2 = map(math.radians, [lat1, lon1, lat2, lon2])

            # Haversine formula
            dlat = lat2 - lat1
            dlon = lon2 - lon1
            a = math.sin(dlat / 2) ** 2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2) ** 2
            c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
            distance = earth_radius * c

            return distance
   
        def return_three_closest(self,lat, lon , graph):
                candidates = []
                queue = []

                for key in graph:
                        if(len(candidates) < 3):
                                heapq.heappush(queue, (self.haversine(lat , lon ,float(graph[key]['lat']) , float(graph[key]['lon']) ), key))
                                
                
                for i in range(0,3):
                       dist , node = heapq.heappop(queue)
                       candidates.append(node)
                return candidates
    

    
    