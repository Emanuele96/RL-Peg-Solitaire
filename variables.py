debug = False

# Board variables
empty_nodes = [(2,2)]
board_form = "triangle"
board_size = 5

#system variables
learning = True
#steps = 50 #steps per episodes
episodes = 1000
visualize = True
frame_delay = 400


# Actor variables
e_actor_start =0.6
e_actor_stop = 0.001
lr_actor = 1.2
eligibility_decay_actor = 0.9
discount_actor = 0.9

# Critic variables
discount_critic = 0.98
lr_critic = 1.2
eligibility_decay_critic = 0.9
initialize_values_range_critic = 2

