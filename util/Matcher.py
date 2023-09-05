import math
import numpy as np
from hmm.HmmProbabilities import HmmProbabilities
from util.Candidate import Candidate
from hmm.Viterbi import Viterbi
from util.CoordinateUtil import CoordinateUtil

class Matcher:
    
    def match(self, graph , coordinates):
        candidates = []
        hidden_states = []

        hmm = HmmProbabilities(4,0.93)
        coordinateUtil = CoordinateUtil()
      
        for i in range(len(coordinates)):
            nearby = coordinateUtil.return_three_closest(coordinates[i][0], coordinates[i][1] , graph)
            inn = []
            counter = 0
          
  
            for j in range(len(nearby)):
                _id = nearby[j]
                near_coord = [graph[nearby[j]]['lat'] , graph[nearby[j]]['lon']]
                counter += 1
                hidden_states.append(_id)
            
                inn.append(Candidate(
                    coordinates[i][0],
                    coordinates[i][1],
                    nearby[j],
                    hmm.emission_probability(near_coord[0], near_coord[1], coordinates[i][0], coordinates[i][1]),
                    str(i)
                ))

            if counter == 0:
                raise Exception("Invalid inputs")

            candidates.append(inn)

        size = len(hidden_states)
        emission_prob = hmm.return_emission_probability(size, len(coordinates), candidates, coordinates)
        transmission_prob = hmm.return_transmission_probability( size, candidates, graph)

 
       
        initial_probability = np.full(size, 1.0 / size)

        viterbi = Viterbi()
        result = viterbi.viterbi(coordinates, hidden_states, initial_probability, transmission_prob, emission_prob, graph)

        return result
             
    