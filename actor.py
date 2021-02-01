import variables
import random

class Actor:

    def __init__(self):
        self.policy = {}
        self.SAP_eligibilities = {}
        self.e_greedy = variables.e_actor_start
        self.lr = variables.lr_actor
        self.eligibility_decay = variables.eligibility_decay_actor
        self.discount = variables.discount_actor
        self.SAPs_in_episode = list(())

    def get_action(self, state, possible_actions):
      
        #Get all SAP for the given state
        relevant_policies = {k:v for k,v in self.policy.items() if k[0]==state}

        if random.random() <= self.e_greedy or len(relevant_policies) == 0:
            #Do a greedy choice
            choosen_action = random.choice(possible_actions)
        else:  
            #Retrieve the SAP with the highest value
            choosen_action = max(relevant_policies, key=relevant_policies.get)[1] #max_policy[1]
            if relevant_policies[(state,choosen_action)] < 0:
                choosen_action = random.choice(possible_actions)
        # add a new key in the policy dict with value 0, if not  SAP existent from before
        if (state, choosen_action) not in self.policy:
            self.policy[(state,choosen_action)] = 0
        return choosen_action

    def update(self, state_t, action_t, TD_error):
        #Get updated TD-error, update policy and eligibilities
        ## Set eligibility last state action pair to be 1
        self.SAP_eligibilities[(state_t, action_t)] = 1

        #Add the SAP in the list of SAPs seen in this episode
        if (state_t, action_t) not in self.SAPs_in_episode:
            self.SAPs_in_episode.append((state_t,action_t))

        for SAP in self.SAPs_in_episode:
        #dinamically initializate new values
            if SAP not in self.SAP_eligibilities:
                self.SAP_eligibilities[SAP] = 0
            if SAP not in self.policy:
                self.policy[SAP] = 0
            self.policy[SAP] =  self.policy[SAP] + self.lr * TD_error * self.SAP_eligibilities[SAP]
            self.SAP_eligibilities[SAP] = self.eligibility_decay * self.discount * self.SAP_eligibilities[SAP]
        
    def reset(self):
        self.SAPs_in_episode = list(())
        self.SAP_eligibilities = {}
        self.e_greedy =  self.e_greedy - ((variables.e_actor_start - variables.e_actor_stop)/ variables.episodes) * 1.05
        if self.e_greedy < 0:
            self.e_greedy = 0