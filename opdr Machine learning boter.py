from bke import MLAgent, is_winner, opponent, start

class MyAgent(MLAgent):
    def evaluate(seld, board):
        if is_winner(board, self.symbol):
            reward = 1
        elif is_winner(board, opponent[self.symbol]):
            reward = -1
        else:
            reward = 0
        return reward