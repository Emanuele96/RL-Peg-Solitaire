import variables
import random
import math

class Actor:

    def __init__(self):
        self.policy = {}
        self.SAP_eligibilities = {}
        self.e_greedy = variables.e_actor_start
        self.lr = variables.lr_actor
        self.eligibility_decay = variables.eligibility_decay_actor
        self.discount = variables.discount_actor
        
    def get_action(self, state, possible_actions):
        # add a new key in the policy dict with value 0, if not SAP existent from before
        for action in possible_actions:
            if (state, action) not in self.policy:
                self.policy[(state, action)] = 0
            if (state, action) not in self.SAP_eligibilities:
                self.SAP_eligibilities[(state, action)] = 0
        #Get all SAP for the given state
        #relevant_policies = list(())#{k:v for k,v in self.policy.items() if k[0]==state}
        max_policy_value = -math.inf
        max_policy = None
        for SAP in self.policy.keys():
            if SAP[0] == state:
                #relevant_policies.append(SAP)
                if self.policy[SAP] >= max_policy_value:
                    max_policy_value = self.policy[SAP]
                    max_policy = SAP

        if random.random() <= self.e_greedy:
            #Do a greedy choice
            choosen_action = random.choice(possible_actions)
        else:  
            #Retrieve the SAP with the highest value
            choosen_action = max_policy[1] #max(relevant_policy, key=relevant_policy.get)[1]
        #update eligibility for that SAP pair
        self.SAP_eligibilities[(state,choosen_action)] = 1
        return choosen_action

    def update(self, state_t, action_t, TD_error):
        #Get updated TD-error, update policy and eligibilities

        #dinamically initializate new values
        '''if (state_t, action_t) not in self.policy.keys():
            self.policy[(state_t, action_t)] = 0
        if (state_t, action_t) not in self.SAP_eligibilities.keys():
            self.SAP_eligibilities[(state_t, action_t)] = 0
        '''

        for SAP in self.policy.keys():
            self.policy[SAP] =  self.policy[SAP] + self.lr * TD_error * self.SAP_eligibilities[SAP]
        for SAP in self.SAP_eligibilities:
            self.SAP_eligibilities[SAP] = self.eligibility_decay * self.discount * self.SAP_eligibilities[SAP]
        ## Set eligibility last state action pair to be 1
        self.SAP_eligibilities[(state_t, action_t)] = 1
        
    def reset_eligibility(self):
        for SAP in self.SAP_eligibilities:
            self.SAP_eligibilities[SAP] = 0
        self.e_greedy = self.e_greedy - ((variables.e_actor_start - variables.e_actor_stop)/ variables.episodes)