import numpy as np
import json

class Viterbi:
    def argmax(self, array):
        max_index = np.argmax(array)
        return max_index

    def viterbi(self, observation_sequence, states, start_probabilities, transition_probabilities, emission_probabilities):
        num_states = len(states)
        T = len(observation_sequence)

      
        observation_mapping = {observation_sequence[i][0]: i for i in range(T)}

    
        trellis = np.zeros((num_states, T))

      
        backpointers = np.zeros((num_states, T), dtype=int)

        # Set the initial values in the trellis
        for i in range(num_states):
            observation_index = observation_mapping[observation_sequence[0][0]]
            trellis[i][0] = start_probabilities[i] * emission_probabilities[i][observation_index]
            backpointers[i][0] = 0

        # forward pass of the Viterbi algorithm
        for t in range(1, T):
            for i in range(num_states):
                probabilities = np.zeros(num_states)
                for j in range(num_states):
                    probabilities[j] = trellis[j][t - 1] * transition_probabilities[j][i]
                max_index = self.argmax(probabilities)
                observation_index = observation_mapping[observation_sequence[t][0]]
                trellis[i][t] = probabilities[max_index] * emission_probabilities[i][observation_index]
                backpointers[i][t] = max_index

        # backward pass to find the most likely state sequence
        state_sequence = np.zeros(T, dtype=int)
        state_sequence[T - 1] = self.argmax(trellis[:, T - 1])
        for t in range(T - 2, -1, -1):
            state_sequence[t] = backpointers[state_sequence[t + 1]][t + 1]
       
        return state_sequence

