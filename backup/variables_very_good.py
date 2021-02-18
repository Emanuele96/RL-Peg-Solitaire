debug = False

# Board variables: Diamond (3-6) and Triangle (4-8)
empty_nodes = [(2,1)]
board_form = "triangle"
board_size = 5

#system variables
learning = True
episodes = 1000
visualize = True
frame_delay = 10
terminal_goal_state_reward = 1000
terminal_state_penalty = -10
non_terminal_state_reward = 1
games_to_visualize = 1

# Actor variables
random_seed_actor = 42
e_actor_start = 0.5
e_actor_stop = 0.001
#e_decay suggested: 0.995 for 1000 epochs and 0.9995 for 10000 epochs
e_decay = 0.995 
lr_actor = 0.1
eligibility_decay_actor = 0.95
discount_actor = 0.95
# "decay", "variable_decay" and "linear"
decay_function = "variable_decay"
total_greedy_percent = 0.1

# Critic variables
#"table" or "function"
state_value_source = "function"
random_seed_critic = 24
discount_critic = 0.95
lr_critic_table = 0.1
eligibility_decay_critic = 0.95
initialize_values_range_critic = 0.1
nn_layers =  [20, 30, 5, 1]
lr_critic_function = 5*10e-4