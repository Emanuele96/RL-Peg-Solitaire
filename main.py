import game
import actor
import critic
import variables
import matplotlib.pyplot as plt
from progress.bar import IncrementalBar



if __name__ == "__main__":  
    #initializate variables
    actor_module = actor.Actor()
    critic_module = critic.Critic(actor_module)
    left_pegs_list = list(())
    episode_number = list(())
    game = game.Game(actor_module, critic_module, False)
    bar = IncrementalBar('Training', max=variables.episodes)
    #start a game, an episode
    for i in range(variables.episodes):
        if i == variables.episodes - 1:
            visualize = True
        else: 
            visualize = False
        critic_module.reset_eligibility()
        actor_module.reset_eligibility()
        
        #print("Start game nr " + str(i + 1))
        game.reset(visualize)
        left_pegs = game.start_game()
        episode_number.append(i)
        left_pegs_list.append(left_pegs)
        bar.next()
    bar.finish()
    plt.plot(episode_number, left_pegs_list) 
    plt.xlabel('Episode nr') 
    plt.ylabel('Left pegs') 
    plt.title('Stats') 
    plt.show() 