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

    def start_game(self, visualize, train):
        #Begin a new episode, get the initial state and legal actions then choose an initial action
        self.reset(visualize)
        state_t = self.board.get_state()
        all_legal_actions_t = self.board.find_all_legal_actions()
        action_t = self.player.get_action(state_t, all_legal_actions_t) 
        if self.visualize:
            pygame.init()
            effect_step = pygame.mixer.Sound('step.wav')
            #Show start board, generate an img, get the size and initializate a pygame display
            img = self.board.show_board()
            X, Y = img.size
            display_surface = pygame.display.set_mode((X,Y)) 
            frame = self.pil_image_to_pygame(img)
            pygame.display.set_caption('Peg Solitaire - Emanuele Caprioli')
            display_surface.blit(frame, (0, 0)) 
            pygame.display.update() 
            pygame.time.delay(variables.frame_delay)
            last_pil_frames = None

        while (not self.game_over) or self.visualize:
            if not self.game_over:
                #Update the board with the action t
                new_pil_frames = self.board.update(action_t)
                #get the new state from the board
                state_t1 = self.board.get_state()
                #Get all the legal actions
                all_legal_actions_t1 = self.board.find_all_legal_actions()
                if len(all_legal_actions_t1) > 0:
                    # If there are legal actions, let the player choose next action
                    action_t1 = self.player.get_action(state_t1, all_legal_actions_t1)
                else:
                    # else set game to be over on this round
                    action_t1 = None
                    self.game_over = True
                # get the reward from the board
                reward_t1 = self.board.get_reward(self.game_over)
                #update the player with the state the board is in, eventual rewards and list of possible actions
                self.player.update(state_t, state_t1, action_t, reward_t1, train)
                # set St = St+1 and At = At+1, repeat the loop if not game over
                state_t = state_t1
                action_t = action_t1

            if self.visualize:
                #Performe the routine for visualization
                if new_pil_frames != last_pil_frames:
                    new_frames = (self.pil_image_to_pygame(new_pil_frames[0]) ,  self.pil_image_to_pygame(new_pil_frames[1]) )
                    last_pil_frames = new_pil_frames
                    # Update the pygame display with the new frames a delay between each frames
                    display_surface.blit(new_frames[0], (0, 0)) 
                    pygame.display.update() 
                    pygame.time.wait(variables.frame_delay)
                    display_surface.blit(new_frames[1], (0, 0)) 
                    pygame.display.update() 
                    effect_step.play()
                    pygame.time.wait(variables.frame_delay)
                    effect_step.stop()
                for event in pygame.event.get() :
                    if event.type == pygame.QUIT :
                        pygame.quit()
                        return self.calculate_left_pegs()
        return self.calculate_left_pegs()
                           
    # Convert a PIL object to a Pygame image object
    def pil_image_to_pygame(self, pilImage):
        return pygame.image.fromstring(
            pilImage.tobytes(), pilImage.size, pilImage.mode).convert()
        
    def calculate_left_pegs(self):
        return len(self.board.state_t.replace('0',''))
    #Reset the game to initial condition, so to be run again as a new episode. 
    # For performance reasons: it does not have to compute the same board for each episode.
    def reset(self, visualize):
        self.visualize = visualize
        self.board.reset(visualize)
        self.game_over = False