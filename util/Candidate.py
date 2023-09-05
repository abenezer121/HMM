


class Candidate:
    def __init__(self , lat , lon , nodeId, emission_probability = 0,id = "" ):
        self.latitude = lat 
        self.longitude = lon
        self.nodeId = nodeId
        self.emission_probability = emission_probability
        self.id = id

    def get_nodeid(self):
        return self.nodeId
    def get_id(self):
        return self.id
    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude
  
    def get_emission_probability(self):
        return self.emission_probability



