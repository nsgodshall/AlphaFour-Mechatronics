# import resetBeltController 
# import elevatorBeltController
# import dropperController
import gameParser

def main():
    # rc = resetBeltController.resetBeltController()
    # dc = dropperController.dropperController()
    # ec = elevatorBeltController.elevatorBeltController()
    gp = gameParser.gameParser()
    # gp.addMoveToGameState(3)
    print(gp.queryGame())
    
main()