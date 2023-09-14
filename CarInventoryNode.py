
from Car import Car

class CarInventoryNode(Car):

    def __init__(self, car):
        
        self.make = car.make
        self.model = car.model
        
        self.cars = []
        self.cars.append(car)
        self.parent = None
        self.left = None
        self.right= None

    def getMake(self):
        return self.make

    def getModel(self):
        return self.model

    def getParent(self):
        if self.parent:
            return self.parent
        else:
            return None

    def setParent(self, parent):
        self.parent = parent

    def getLeft(self):
        if self.left:
            return self.left
        else:
            return None

    def setLeft(self, left):
        if self.left ==None:
            self.left = CarInventoryNode(left)
        else:
            t = CarInventoryNode(left)
            t.left = self.left
            self.left = t

    def getRight(self):
        if self.right:
            return self.right
        else:
            return None
    def setRight(self, right):
        if self.right==None:
            self.right = CarInventoryNode(right)
        else:
            t = CarInventoryNode(right)
            t.right = self.right
            self.right = t

    def __str__(self):

        s=''
        for cars in self.cars:
            s += str(cars)
            s+= '\n'
        return s
        
car1 = Car("Dodge", "dart", 2015, 6000)
car2 = Car("dodge", "DaRt", 2003, 5000)
car3 = Car('Chevy', 'Volt', 2015, 15000)
carNode = CarInventoryNode(car1)
carNode.cars.append(car2)
carNode.setRight(car3)

car4 = Car('Toyota', 'Prius', 2007, 6500)
carNode.setLeft(car4)
    

    
