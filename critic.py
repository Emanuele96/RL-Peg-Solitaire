import variables
import random
class Critic:
    def __init__(self, actor):
        self.actor = actor
        self.state_values = {}
        self.state_eligibility = {}
        self.discount_factor = variables.discount_critic
        self.lr = variables.lr_critic
        self.e_decay = variables.eligibility_decay_critic
        self.states_in_episode = list(())

    def update(self, state_t, state_t1, action_t, reward_t1):
        #append the state in the list of states in this episode
        if state_t not in self.states_in_episode:
            self.states_in_episode.append(state_t)
        #Calculate TD error
        TD_error = self.calculate_TD_error(reward_t1, state_t, state_t1)
        # Set eligibility for state t = 1
        self.state_eligibility[state_t] = 1
        #Send TD error to actor, trigger actor update routine
        self.actor.update(state_t, action_t, TD_error)
        for state in self.states_in_episode:
            #Update value table for each state 
            self.update_value_table(state, TD_error)
            #update eligibility for each state 
            self.state_eligibility[state] = self.discount_factor * self.e_decay * self.state_eligibility[state]


    def reset(self):
        self.states_in_episode = list(())
        #for state in self.state_eligibility:
        #    self.state_eligibility[state] = 0
        self.state_eligibility = {}

    #fill a list of all permutation of a binary number of length n. Used to generate all possible states of the board.
    def generate_all_binary_states(self, n, result, bs = ''):
        if n:
            self.generate_all_binary_states(n-1 , result,  bs + '0')
            self.generate_all_binary_states(n-1, result, bs + '1')
        else:
            result.append(bs)

    def calculate_TD_error(self, reward_t1, state_t, state_t1):
        if state_t not in self.state_values:
            self.state_values[state_t] = random.uniform(0,variables.initialize_values_range_critic)
        if state_t1 not in self.state_values:
            self.state_values[state_t1] = random.uniform(0,variables.initialize_values_range_critic)
        return reward_t1 + self.discount_factor * self.state_values[state_t1] - self.state_values[state_t]

    def update_value_table(self, state_t, TD_error):
        if state_t not in self.state_eligibility:
            self.state_eligibility[state_t] = 0
        self.state_values[state_t] = self.state_values[state_t] + self.lr * TD_error * self.state_eligibility[state_t]