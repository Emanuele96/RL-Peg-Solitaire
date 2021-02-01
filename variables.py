debug = False

# Board variables: Diamond (3-6) and Triangle (4-8)
empty_nodes = [(2,2),(1,1)]
board_form = "diamond"
board_size = 5

#system variables
learning = True
episodes = 50000
visualize = True
frame_delay = 400
terminal_goal_state_reward = 100
terminal_state_penalty = 0
non_terminal_state_reward = 0

# Actor variables
e_actor_start = 0.5
e_actor_stop = 0.001
e_decay = 0.98
lr_actor = 1
eligibility_decay_actor = 0.88
discount_actor = 0.9

# Critic variables
discount_critic = 0.9
lr_critic = 1
eligibility_decay_critic = 0.88
initialize_values_range_critic = 5
