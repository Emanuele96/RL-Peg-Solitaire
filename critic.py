class Critic:
    def __init__(self, actor):
        self.actor = actor
    def update(self, state_t, state_t1, action_t, action_t1, reward_t1):
        return  -1