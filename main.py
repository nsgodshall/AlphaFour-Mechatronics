import resetBeltController 
import elevatorBeltController
import dropperController

def main():
    rc = resetBeltController.resetBeltController()
    dc = dropperController.dropperController()
    ec = elevatorBeltController.elevatorBeltController()

    rc.test()
    dc.test()
    ec.test()
main()