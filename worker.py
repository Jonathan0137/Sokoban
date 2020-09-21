

class worker(object):
    def __init__(self, myLevel):
        """Constructor for worker class. Takes init worker location and save it as x and y

        Args:
            myLevel (Level): A level object to get init worker location from txt file
        """
        self.x = myLevel.getWorkerLocation()[0]
        self.y = myLevel.getWorkerLocation()[1]
    def moveWorkerCorr(self, x, y):
        """Move worker location

        Args:
            x (int): worker's x corrd
            y (int): worker's y corrd
        """
        self.x = x
        self.y = y
    def update(self, myLevel, Simplematrix, direction):
        """Update worker location and matrix

        Args:
            myLevel (Level): Level object to update to
            Simplematrix (list[str]): a updated simplematrix to be uploaded to myLevel
            direction (str): direction of the worker
        """
        myLevel.updateMatrixGivenSimpleMatrix(Simplematrix)
        myLevel.updateWorkerLocation(self.x, self.y, direction)

    def find_type_of_object(self, box):
        """get the type of the object

        Args:
            box (str): can be one of '0, 1, 2, 3, 4' which means "ground, wall, box, targetGround, box_in_correct_location"

        Returns:
            [str]: returns "ground, wall, box, targetGround, box_in_correct_location" given input
        """
        if(box == '0'):
            return "ground"
        elif(box == '1'):
            return "wall"
        elif(box == '2'):
            return "box"
        elif(box == '3'):
            return "targetGround"
        elif(box == '4'):
            return "box_in_correct_location"

    def moveContent(self, x, y, Simplematrix):
        """Move the content given worker current location, 
        simple matrix and how much you want to move for

        Args:
            x (int): how much do you want to move in the x direction
            y (int): how much do you want to move in the y direction
            Simplematrix (list[str]): Simple matrix reprsenting the board
        """
        next_box = Simplematrix[self.y+y][self.x+x]
        type_of_next_object = self.find_type_of_object(next_box)

        if(type_of_next_object == "ground"):#print("This is a ground")
            self.moveWorkerCorr(self.x+x, self.y+y)
        elif(type_of_next_object == "box"):#print("This is a box")
            if(self.find_type_of_object(Simplematrix[self.y+y+y][self.x+x+x]) == "ground"): # see if object after box is ground
                Simplematrix[self.y+y+y][self.x+x+x] = '2'
                self.moveWorkerCorr(self.x+x, self.y+y)
                Simplematrix[self.y][self.x] = '0'
            elif(self.find_type_of_object(Simplematrix[self.y+y+y][self.x+x+x]) == "targetGround"):# see if object after box is targetGround
                Simplematrix[self.y+y+y][self.x+x+x] = '4'
                self.moveWorkerCorr(self.x+x, self.y+y)
                Simplematrix[self.y][self.x] = '0'

        elif(type_of_next_object == "targetGround"):
            #"This is a targetGround"
            self.moveWorkerCorr(self.x+x, self.y+y)

        elif(type_of_next_object == "box_in_correct_location"):
            #print("This is a box_in_correct_location")
            if(self.find_type_of_object(Simplematrix[self.y+y+y][self.x+x+x]) == "ground"): # see if object after box is ground
                Simplematrix[self.y+y+y][self.x+x+x] = '2'
                self.moveWorkerCorr(self.x+x, self.y+y)
                Simplematrix[self.y][self.x] = '0'
            elif(self.find_type_of_object(Simplematrix[self.y+y+y][self.x+x+x]) == "targetGround"):# see if object after box is targetGround
                Simplematrix[self.y+y+y][self.x+x+x] = '4'
                self.moveWorkerCorr(self.x+x, self.y+y)
                Simplematrix[self.y][self.x] = '3'



    def movePlayer(self, direction, myLevel):
        """Move worker given its direction, current location, and it's level

        Args:
            direction (str): worker's direction
            myLevel (Level): a instance of Level for level number, simplematrix.
        """
        Simplematrix = myLevel.getSimpleMatrix()

        if(direction == "up"):
            #print("+++++++++MOVING UP++++++++++")
            self.moveContent(0, -1, Simplematrix)
            
        elif(direction == "down"): 
            #print("+++++++++MOVING down++++++++++")
            self.moveContent(0, 1, Simplematrix)

        elif(direction == "left"): 
            #print("+++++++++MOVING left++++++++++")
            self.moveContent(-1, 0, Simplematrix)
            
        elif(direction == "right"): 
            #print("+++++++++MOVING right++++++++++")
            self.moveContent(1, 0, Simplematrix)

        self.update(myLevel, Simplematrix, direction)


