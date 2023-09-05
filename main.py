import csv 
import sys
from util.Graph  import Graph
from util.Matcher import Matcher

          
if __name__ == "__main__":
    
    coordinates = [[9.0246348,38.8163494],
    [9.0116678,38.8007156],
    [9.0218942,38.8142232],
    [9.021704,38.8142719],
    [9.0215161,38.8136935]]
    g = Graph()
    matcher = Matcher()
    graph = g.read_graph()
    matcher.match(graph , coordinates)



