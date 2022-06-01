import subprocess as sp

class gameParser: 
    def __init__(self):
        self.gameState = "242424"
    
    def addMoveToGameState(self, playerMove):
        self.gameState += str(playerMove)
    
    def queryGame(self):
        p = sp.run(["./alphaFourBind", self.gameState], capture_output = True)
        move = p.stdout.decode()
        self.addMoveToGameState(move)
        return move
        