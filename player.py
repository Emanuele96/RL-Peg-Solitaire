import variables

class Player:
    def __init__(self, actor, critic):       
        self.learning = variables.learning
        self.actor = actor
        self.critic = critic

    
    def update(self, state_t, state_t1, action_t, reward_t1, train):
        if train:
            self.critic.update(state_t, state_t1, action_t, reward_t1)
        #update the player with the passed values of state the board is in, eventual rewards and list of possible actions
       ## self.states.append(new_state)
       ## self.rewards.append(new_reward)
        #Don't update the critic when on initial state or if it is not learning
       ## if len(self.states) != 1 and self.learning:
         ##   self.critic.update(self.states[-2], self.states[-1], self.actions[-1], self.rewards[-1] )
        ##if not game_over:
            #Choose a new action from the legal ones
         ###   new_action = self.actor.get_action(new_state, possible_actions)
         ##   self.actions.append(new_action)
         
    def get_action(self, state, possible_actions):
        return self.actor.get_action(state, possible_actions) 



