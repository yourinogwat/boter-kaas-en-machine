from bke import MLAgent, is_winner, opponent, start, train, save

class MyAgent(MLAgent):
    def evaluate(self, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward
    
actualGod = MyAgent()

train(actualGod, 3000)

save(actualGod, 'trainedGod')

start(player_x = actualGod)