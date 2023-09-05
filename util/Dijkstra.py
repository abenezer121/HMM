import heapq

class Dijkstra:

    def dijkstra(self, graph , sourceId , destinationId):
        distance = {} 
        distance[sourceId] = 0
       
        queue = [(0 , sourceId)] 

        while queue:
            dist , node = heapq.heappop(queue)
       
            for neighbor,weight in graph[node].items():
                new_dist = dist + weight

                if neighbor not in distance or new_dist < distance[neighbor]:
                    distance[neighbor] = new_dist
                    # add to the queue
                    heapq.heappush(queue, (distance, neighbor))


                    queue.sort()
        if destinationId not in distance:
            return 1000000000
        return distance[destinationId]



#  graph = {
#         'A': {'B': 1, 'C': 4},
#         'B': {'A': 1, 'C': 2, 'D': 5},
#         'C': {'A': 4, 'B': 2, 'D': 1},
#         'D': {'B': 5, 'C': 1}
# }