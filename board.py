class Board:

    def __init__(self, cards):
        self.drawpile = cards
        self.player = []
        self.discard = []
    
    # Add Player
    def addPlayer(self, newPlayer):
        self.player.append(newPlayer)
    
    # Update Player
    def update(self):
        for i in self.player:
            i.update()