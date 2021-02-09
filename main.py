import game
import actor
import critic
import variables
import matplotlib.pyplot as plt
from progress.bar import IncrementalBar



if __name__ == "__main__":  
    #initializate actor and critic modules
    actor_module = actor.Actor()
    critic_module = critic.Critic(actor_module)
    # Initializate lists used for plots
    left_pegs_list = list(())
    episode_number = list(())
    e_greedy_list = list(())
    game = game.Game(actor_module, critic_module, False)
    bar = IncrementalBar('Training', max=variables.episodes)
    #start a game, an episode and visualize only the last games. Append the remaining pegs per episode
    for i in range(variables.episodes):
        if i >= variables.episodes - variables.games_to_visualize:
            visualize = True
        else: 
            visualize = False
        # Run reset routine for Actor and Critic at the end of each episode
        critic_module.reset()
        actor_module.reset()
        #Run an episode and append results to plot lists
        left_pegs = game.start_game(visualize, train=True)
        episode_number.append(i)
        left_pegs_list.append(left_pegs)
        e_greedy_list.append(actor_module.e_greedy)
        bar.next()
    bar.finish()

    #Plot the graph with the remaining pegs.
    color = 'tab:blue'
    fig, ax1 = plt.subplots()

    ax1.set_xlabel('Episode nr')
    ax1.set_ylabel('Left pegs', color=color)
    ax1.plot(episode_number, left_pegs_list, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    color = 'tab:red'
    ax2 = ax1.twinx()  
    ax2.set_ylabel('sigma', color=color)  
    ax2.plot(episode_number, e_greedy_list, color=color)
    ax2.tick_params(axis='y', labelcolor=color)


    fig.tight_layout()
    plt.show()

    