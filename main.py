import simworld
import player
import variables

if __name__ == "__main__":  
    board = simworld.Board(variables.board_form, variables.board_size, variables.empty_nodes)
    board.show_board()
