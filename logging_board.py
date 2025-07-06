from board import Board

class LoggingBoard(Board):
    def __init__(self):
        super().__init__()
        self.log = []

    def claim_square(self, player, index):
        super().claim_square(player, index)
        self.log.append(f"{player.name} PICKED SQUARE {index}")

    def get_winner(self):
        winner = super().get_winner()
        if winner:
            self.log.append(f"{winner.name} WINS THE GAME")
        return winner

    def game_over(self):
        over = super().game_over()
        if over:
            for entry in self.log:
                print(entry)
        return over
