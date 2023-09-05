import csv 

class Graph:
    def __init__(self):
        self.graph = {}

    def read_graph(self):
 
        with open('data/node.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            spamreader.__next__()
            for row in spamreader:
                if(int(row[0]) <= 1629):
                    self.graph[int(row[0])] = {'lat' : float(row[1]) , 'lon' : float(row[2])}


        with open('data/edges.csv', newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            spamreader.__next__()
            for row in spamreader:
             
                if len(row) == 3 and (int(row[0]) <= 1629 and int(row[1]) <= 1629):
                    self.graph[int(row[0])][int(row[0])] = float(row[2])
        return self.graph    

