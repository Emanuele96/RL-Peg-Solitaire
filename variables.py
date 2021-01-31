debug = False

# Board variables
empty_nodes = [(0,0)]
board_form = "diamond"
board_size = 6

#system variables
learning = True
number_of_moves = 50 #steps per episodes
visualize = True
frame_delay = 400


# Actor variables
e_actor = 1
lr_actor = 0.9
eligibility_decay_actor = 0.99
discount_actor = 0.9

# Critic variables
discount_critic = 0.95
lr_critic = 1
eligibility_decay_critic = 0.9
initialize_values_range_critic = 5