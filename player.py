import variables

class Player:
    def __init__(self, actor, critic):       
        self.learning = variables.learning
        self.actor = actor
        self.critic = critic

    
    def update(self, state_t, state_t1, action_t, reward_t1, train):
        if train:
        #update the player with the passed values of state the board is in, eventual rewards and list of possible actions
            self.critic.update(state_t, state_t1, action_t, reward_t1)
         
    def get_action(self, state, possible_actions):
        return self.actor.get_action(state, possible_actions) 



