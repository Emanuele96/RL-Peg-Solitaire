import simworld
import player
import variables
import pygame

class Game:
        
    def __init__(self, actor, critic):
        self.player = player.Player(actor, critic)
        self.board = simworld.Board(variables.board_form, variables.board_size, variables.empty_nodes)
        self.game_over = False

    def start_game(self):
        if variables.visualize:
            pygame.init()
            white = (255, 255, 255) 
            X = 650
            Y = 500
            display_surface = pygame.display.set_mode((X, Y )) 
            pygame.display.set_caption('Peg Solitaire')
            #Show start board
            frame = self.pil_image_to_pygame(self.board.show_board())
            display_surface.blit(frame, (0, 0)) 
            pygame.display.update() 
            pygame.time.delay(variables.frame_delay)

        while (not self.game_over) or variables.visualize:
            for i in range(variables.number_of_moves):
                if not self.game_over:
                    #update the player with the state the board is in, eventual rewards and list of possible actions
                    all_legal_actions = self.board.find_all_legal_actions()
                    if len(all_legal_actions) == 0:
                        print("Game Over after " + str(self.board.move_counter) + " moves")
                        self.game_over = True
                        break
                    self.player.update(self.board.state_t, self.board.get_reward(), all_legal_actions)
                    #perform an action choose by the player to the board
                    new_frames = self.board.update(self.player.perform_action())
                if variables.visualize and not self.game_over:
                    # Update the pygame display with the new frames
                    frame_1 = self.pil_image_to_pygame(new_frames[0])
                    frame_2 = self.pil_image_to_pygame(new_frames[1])
                    display_surface.fill(white)
                    display_surface.blit(frame_1, (0, 0)) 
                    pygame.display.update() 
                    pygame.time.delay(variables.frame_delay)
                    display_surface.blit(frame_2, (0, 0)) 
                    pygame.display.update() 
                    pygame.time.delay(variables.frame_delay)
                for event in pygame.event.get() :
                    if event.type == pygame.QUIT :
                        pygame.quit()
                        quit()
                           

    def pil_image_to_pygame(self, pilImage):
        return pygame.image.fromstring(
            pilImage.tobytes(), pilImage.size, pilImage.mode).convert()