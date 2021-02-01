debug = False

# Board variables
empty_nodes = [(2,2)]
board_form = "triangle"
board_size = 5

#system variables
learning = True
steps = 50 #steps per episodes
episodes = 2000
visualize = True
frame_delay = 400


# Actor variables
e_actor =0.5
e_decay = 0.002
lr_actor = 1.12
eligibility_decay_actor = 0.99
discount_actor = 0.98

# Critic variables
discount_critic = 0.98
lr_critic = 1.2
eligibility_decay_critic = 0.9
initialize_values_range_critic = 2