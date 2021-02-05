debug = False

# Board variables: Diamond (3-6) and Triangle (4-8)
empty_nodes = [(0,0)]
board_form = "diamond"
board_size = 6

#system variables
learning = True
episodes = 2000
visualize = True
frame_delay = 100
terminal_goal_state_reward = 10000
terminal_state_penalty = 0
non_terminal_state_reward = 0

# Actor variables
random_seed_actor = 42
e_actor_start = 0.5
e_actor_stop = 0.001
e_decay = 0.995
lr_actor = 1
eligibility_decay_actor = 0.95
discount_actor = 0.95
decay_function = "variable_decay"
total_greedy_percent = 0.001

# Critic variables
random_seed_critic = 24
discount_critic = 0.95
lr_critic = 1
eligibility_decay_critic = 0.95
initialize_values_range_critic = 2