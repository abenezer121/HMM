


class Candidate:
    def __init__(self , lat , lon , road_start , road_end, perpendicular_latitude , perpendicular_longitude , emission_probability = 0, id = "" ):
        self.lat = lat 
        self.lon = lon
        self.road_start = road_start
        self.road_end = road_end
        self.perpendicular_latitude = perpendicular_latitude
        self.perpendicular_longitude = perpendicular_longitude
        self.emission_probability = emission_probability
        self.id = id
    
    def get_latitude(self):
        return self.latitude

    def get_longitude(self):
        return self.longitude

    def get_road_start(self):
        return self.road_start

    def get_road_end(self):
        return self.road_end

    def get_perpendicular_latitude(self):
        return self.perpendicular_latitude

    def get_perpendicular_longitude(self):
        return self.perpendicular_longitude
    
    def get_emission_probability(self):
        return self.emission_probability
