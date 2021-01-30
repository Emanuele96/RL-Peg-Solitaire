class Player:
    def __init__(self, actor, critic):
        #state at time t
        self.state_t = None
        #list of possible actions at time t
        self.possible_actions = list(())
        #choosen action to perform at time t
        self.action_t = None
        #received reward at time t+1
        self.reward_t1 = None
        #a list (ordered) containing all performed state-action pairs
        self.performed_actions = list(())
        self.actor = actor
        self.critic = critic

    def perform_an_action(self):
        #call the actor, pass the state t and get an action a and perform it on the board.
        return -1
    
    def update(self):
        #update the player with the new state, 
        return -1
