import game
import actor
import critic
import variables

if __name__ == "__main__":  
    #initializate variables
    actor_module = actor.Actor()
    critic_module = critic.Critic(actor_module)
    

    #start a game, an episode
    for i in range(variables.episodes):
        if i == variables.episodes - 1:
            visualize = True
        else: 
            visualize = False
        critic_module.reset_eligibility()
        actor_module.reset_eligibility()
        episode = game.Game(actor_module, critic_module, visualize)
        print("Start game nr " + str(i + 1))
        episode.start_game()