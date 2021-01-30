import simworld
import player
import variables

class Game:
        
    def __init__(self, actor, critic):
        self.player = player.Player(actor, critic)
        self.board = simworld.Board(variables.board_form, variables.board_size, variables.empty_nodes)

    def start_game(self):
        self.board.show_board()
        for i in range(variables.number_of_moves):
            #update the player with the state the board is in, eventual rewards and list of possible actions
            all_legal_actions = self.board.find_all_legal_actions()
            if len(all_legal_actions) == 0:
                print("Game Over")
                self.board.show_board()
                break
            self.player.update(self.board.state_t, self.board.get_reward(), all_legal_actions)
            #perform an action choose by the player to the board
            self.board.update(self.player.perform_action())