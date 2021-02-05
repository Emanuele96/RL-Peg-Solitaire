import variables
import random
import numpy as np
import ann_model
import torch
import torch.optim as optim
import torch.nn as nn

class Critic:
    def __init__(self, actor):
        self.losses = list(())
        self.steps = list(())
        self.step_count = 0
        self.actor = actor
        self.type = variables.state_value_source
        random.seed(variables.random_seed_critic)

        if  self.type == "table":
            self.state_values = {}
            self.state_eligibility = {}
            self.discount_factor = variables.discount_critic_table
            self.lr = variables.lr_critic_table
            self.e_decay = variables.eligibility_decay_critic
            self.states_in_episode = list(())

        elif self.type == "function":
            self.lr = variables.lr_critic_function
            self.discount_factor = variables.discount_critic_function
            if torch.cuda.is_available():
                self.device = "cpu"
            else:
                self.device = "cpu"
            self.nn_layers = variables.nn_layers
            if variables.board_form == "diamond":
                self.input_size = variables.board_size **2
            elif variables.board_form == "triangle":
                self.input_size = 0
                for i in range(1,variables.board_size + 1):
                    self.input_size += i
            self.model = ann_model.Net(self.input_size,self.nn_layers)
            self.optimizer =  optim.SGD(self.model.parameters(), lr=self.lr)
            self.loss = nn.MSELoss(reduction="mean")

            '''print(self.model)
            for name, param in self.model.named_parameters():
                if param.requires_grad:
                    print (name, param.data)
            '''

    def update(self, state_t, state_t1, action_t, reward_t1):
        if self.type == "table":
            value_state_t = self.state_values.setdefault(state_t, random.uniform(0,variables.initialize_values_range_critic))
            value_state_t1 = self.state_values.setdefault(state_t1, random.uniform(0,variables.initialize_values_range_critic))
            #Calculate TD error
            TD_error = self.calculate_TD_error(reward_t1, value_state_t, value_state_t1)
            #append the state in the list of states in this episode
            if state_t not in self.states_in_episode:
                self.states_in_episode.append(state_t)
            # Set eligibility for state t = 1
            self.state_eligibility[state_t] = 1
            for state in self.states_in_episode:
                #Update value table for each state 
                self.update_value_table(state, TD_error)
                #update eligibility for each state 
                self.state_eligibility[state] = self.discount_factor * self.e_decay * self.state_eligibility[state]
        
        elif self.type == "function":
            t = torch.from_numpy(np.fromiter(state_t, dtype= int)).float().to(self.device)
            t1 = torch.from_numpy(np.fromiter(state_t1, dtype=int)).float().to(self.device)
            value_state_t = self.model(t)
            value_state_t1 = self.model(t1)
            #Calculate TD error
            TD_error = self.calculate_TD_error(reward_t1, value_state_t, value_state_t1)
            #to delete
            label = TD_error + value_state_t
            loss = self.loss(value_state_t, label)
            self.losses.append(loss.item())
            self.step_count += 1
            self.steps.append(self.step_count)
            loss.backward()
            self.optimizer.step()
            self.optimizer.zero_grad()


        #Send TD error to actor, trigger actor update routine
        self.actor.update(state_t, action_t, TD_error)


    def reset(self):
        if self.type == "table":
            self.states_in_episode.clear()
            self.state_eligibility.clear()

    def calculate_TD_error(self, reward_t1, value_state_t, value_state_t1):
        return reward_t1 + self.discount_factor * value_state_t1 - value_state_t

    def update_value_table(self, state_t, TD_error):
        self.state_values[state_t] = self.state_values[state_t] + self.lr * TD_error * self.state_eligibility[state_t]