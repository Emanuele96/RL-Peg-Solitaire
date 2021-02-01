import simworld
import player
import variables
import pygame

class Game:
        
    def __init__(self, actor, critic, visualize):
        self.visualize = visualize
        self.player = player.Player(actor, critic)
        self.board = simworld.Board(variables.board_form, variables.board_size, variables.empty_nodes, visualize)
        self.game_over = False

    def start_game(self):
        #Begin a new episode
        self.game_over = False
        if self.visualize:
            pygame.init()
            #white = (255, 255, 255) 
            #Show start board, generate an img, get the size and initializate a pygame display
            img = self.board.show_board()
            X, Y = img.size
            display_surface = pygame.display.set_mode((X,Y)) 
            frame = self.pil_image_to_pygame(img)
            pygame.display.set_caption('Peg Solitaire - Emanuele Caprioli')
            display_surface.blit(frame, (0, 0)) 
            pygame.display.update() 
            pygame.time.delay(variables.frame_delay)

        while (not self.game_over) or self.visualize:
            for i in range(variables.steps):
                if not self.game_over:
                    #update the player with the state the board is in, eventual rewards and list of possible actions
                    all_legal_actions = self.board.find_all_legal_actions()
                    if len(all_legal_actions) == 0:
                        #print("Game Over after " + str(self.board.move_counter) + " moves")
                        self.game_over = True
                        #break
                    self.player.update(self.board.state_t, self.board.get_reward(self.game_over), all_legal_actions, self.game_over)
                    #perform an action choose by the player to the board
                    new_frames = self.board.update(self.player.perform_action())
                if self.visualize and not self.game_over:
                    # Update the pygame display with the new frames
                    frame_1 = self.pil_image_to_pygame(new_frames[0])
                    frame_2 = self.pil_image_to_pygame(new_frames[1])
                    #display_surface.fill(white)
                    display_surface.blit(frame_1, (0, 0)) 
                    pygame.display.update() 
                    pygame.time.delay(variables.frame_delay)
                    display_surface.blit(frame_2, (0, 0)) 
                    pygame.display.update() 
                    pygame.time.delay(variables.frame_delay)
                if self.visualize:
                    for event in pygame.event.get() :
                        if event.type == pygame.QUIT :
                            pygame.quit()
                            return self.calculate_left_pegs()
                            #quit()
        return self.calculate_left_pegs()
                           

    def pil_image_to_pygame(self, pilImage):
        return pygame.image.fromstring(
            pilImage.tobytes(), pilImage.size, pilImage.mode).convert()
        
    def calculate_left_pegs(self):
        return len(self.board.state_t.replace('0',''))

    def reset(self, visualize):
        self.visualize = visualize
        self.board.reset(visualize)
        self.player.reset()
