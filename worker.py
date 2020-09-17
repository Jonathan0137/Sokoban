

class worker(object):
    def __init__(self, myLevel):
        self.x = myLevel.getWorkerLocation()[0]
        self.y = myLevel.getWorkerLocation()[1]
    def moveWorkerCorr(self, x, y):
        self.x = x
        self.y = y
    def update(self, myLevel, Simplematrix):
        myLevel.updateMatrixGivenSimpleMatrix(Simplematrix)
        myLevel.updateWorkerLocation(self.x, self.y)

    def find_type_of_object(self, box):
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

        self.update(myLevel, Simplematrix)


