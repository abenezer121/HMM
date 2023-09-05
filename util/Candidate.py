


class Candidate:
    def __init__(self , lat , lon ,  perpendicular_latitude , perpendicular_longitude , emission_probability = 0, id = "" ):
        self.latitude = lat 
        self.longitude = lon
  
        self.perpendicular_latitude = perpendicular_latitude
        self.perpendicular_longitude = perpendicular_longitude
        self.emission_probability = emission_probability
        self.id = id
    
    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude



    def get_perpendicular_latitude(self):
        return self.perpendicular_latitude

    def get_perpendicular_longitude(self):
        return self.perpendicular_longitude
    
    def get_emission_probability(self):
        return self.emission_probability
