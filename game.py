import simworld
import player
import actor
import critic
import variables

class Game:
    
    def start_game(self):
        board = simworld.Board(variables.board_form, variables.board_size, variables.empty_nodes)
        board.show_board()
        actor_module = actor.Actor()
        critic_module = critic.Critic(actor_module)
        p1 = player.Player(actor_module, critic_module)
        print(board.find_all_legal_actions())