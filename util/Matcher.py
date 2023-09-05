import math
import numpy as np
from hmm.HmmProbabilities import HmmProbabilities
from util.Candidate import Candidate
# from hmm.Viterbi import Viterbi
from util.CoordinateUtil import CoordinateUtil

class Matcher:
    
    def match(self, graph , coordinates):
        candidates = []
        hidden_states = []

        hmm = HmmProbabilities(4,0.93)
        for i in range(len(coordinates)):
            nearby = CoordinateUtil.return_three_closest(coordinates[i][0], coordinates[i][1] , graph)
            inn = []
            counter = 0

        #     for j in range(len(nearby)):
        #         _id = int(''.join(filter(str.isdigit, nearby[j].getId())))
        #         near_coord = CoordinateUtil.haversine(
        #             coordinates[i][0],
        #             coordinates[i][1],
        #             _id,
        #             graph,
        #             pg.edge
        #         )

        #         dist = CoordinateUtil.haversine(near_coord[0], near_coord[1], coordinates[i][0], coordinates[i][1])

        #         if dist > 200:
        #             continue

        #         counter += 1
        #         hidden_states.append(''.join(filter(str.isdigit, nearby[j].getId())))
        #         id_str = str(i)

        #         inn.append(Candidate(
        #             id_str,
        #             coordinates[i][0],
        #             coordinates[i][1],
        #             int(nearby[j].getSource()),
        #             int(nearby[j].getTarget()),
        #             near_coord[0],
        #             near_coord[1],
        #             hmm.emissionProbability(near_coord[0], near_coord[1], coordinates[i][0], coordinates[i][1], 4)
        #         ))

        #     if counter == 0:
        #         raise Exception("Invalid inputs")

        #     candidates.append(inn)

        # size = len(hidden_states)
        # emission_prob = hmm.returnEmissionProbability(size, len(coordinates), candidates, coordinates)

        # transmission_prob = hmm.returnTransmissionProbability( size, candidates, graph)
        # initial_probability = np.full(size, 1.0 / size)

        # viterbi = Viterbi()
        # result = viterbi.viterbi(coordinates, hidden_states, initial_probability, transmission_prob, emission_prob, graph, pg.edge)

        # return result
             
    