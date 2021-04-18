from bke import MLAgent, is_winner, opponent, start, train, save, validate, plot_validation, RandomAgent, load

class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
actualGod = load('trainedGod')
actualGod.learning = False

validation_agent = RandomAgent()

validation_result = validate(agent_x=actualGod, agent_o=validation_agent, iterations=1000)

plot_validation(validation_result)