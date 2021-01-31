import variables

class Player:
    def __init__(self, actor, critic):
        #state at time t
        self.states = list(())
        #received reward at time t
        self.rewards = list(())
        #a list (ordered) containing all performed actions pairs
        self.actions = list(())

        self.actor = actor
        self.critic = critic

    
    def update(self, new_state, new_reward, possible_actions):
        #update the player with the passed values of state the board is in, eventual rewards and list of possible actions
        new_action = self.actor.get_action(new_state, possible_actions)
        self.actions.append(new_action)
        self.states.append(new_state)
        self.rewards.append(new_reward)
        #Don't update the critic when on initial state or if it is not learning
        if len(self.states) != 1 and variables.learning:
            self.critic.update(self.states[-2], self.states[-1], self.actions[-2], self.actions[-1], self.rewards[-1] )
    
    def perform_action(self):
        if variables.debug:
            print("Selected action to perform " + str(self.actions[-1]))
        return self.actions[-1]
    