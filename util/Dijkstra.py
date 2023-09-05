import heapq

class Dijkstra:

    def dijkstra(self, graph , sourceId , destinationId):
        
        distance = {} 
        distance[sourceId] = 0
        queue = [(0 , sourceId)]

        while queue:
            dist , node = heapq.heappop(queue)
            
            for k in graph[node].keys():
                if k not in ('lat', 'lon'):
                    
                    neighbor = k
                    weight = graph[node][k]
          
                    new_dist = dist + float(weight)
                    if neighbor not in distance or new_dist < distance[neighbor]:
                        distance[neighbor] = new_dist
                        heapq.heappush(queue, (new_dist, neighbor))

        if destinationId not in distance:
            return 1000000000
        return distance[destinationId]




