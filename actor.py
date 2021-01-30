import variables
import random

class Actor:

    def __init__(self):
        self.policy = {}
        self.e = variables.e_actor
        self.lr = variables.lr_actor

    def get_action(self, state, possible_actions):
        # add a new key in the policy dict with value 0, if not SAP existent from before
        for action in possible_actions:
            if (state, action) not in self.policy:
                self.policy[(state, action)] = 0
        #Get all SAP for the given state
        relevant_policy = {k:v for k,v in self.policy.items() if k[0]==state}
        
        if random.random() <= variables.e_actor:
            #Do a greedy choice
            choosen_action = random.choice(list(relevant_policy.keys()))
        else:  
            #Retrieve the SAP with the highest value
            choosen_action = max(relevant_policy, key=relevant_policy.get)
        return choosen_action[1]