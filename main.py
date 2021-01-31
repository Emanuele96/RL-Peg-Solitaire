import game
import actor
import critic

if __name__ == "__main__":  
    #initializate variables
    actor_module = actor.Actor()
    critic_module = critic.Critic(actor_module)
    game = game.Game(actor_module, critic_module)

    #start a game, an episode
    critic_module.reset_eligibility()
    actor_module.reset_eligibility()
    game.start_game()