import csv 

class Graph:
    def __init__(self):
        self.graph = {}

    def read_graph(self):
 
        with open('data/node.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            spamreader.__next__()
            for row in spamreader:
                self.graph[int(row[0])] = {'lat' : float(row[1]) , 'lon' : float(row[2])}


        with open('data/edges.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            spamreader.__next__()
            for row in spamreader:
                newdict = {int(row[1]) : float(row[2])}
                self.graph[int(row[0])].update(newdict)
            
        return self.graph    

