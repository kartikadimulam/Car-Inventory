from Car import Car
from CarInventoryNode import CarInventoryNode

class CarInventory:

    def __init__(self):

        self.root = None


    def addCar(self, car):
        if self.root:
            self._addCar(car, self.root)
        else:
            self.root = CarInventoryNode(car)

    def _addCar(self, car, currentNode):

        if car.make < currentNode.make:
            if currentNode.left != None:
                self._addCar(car, currentNode.left)
            else:
                currentNode.left = CarInventoryNode(car)
                
        elif car.make == currentNode.make and car.model < currentNode.model:
            if currentNode.left != None:
                self._addCar(car, currentNode.left)
            else:
                currentNode.left = CarInventoryNode(car)
                
        elif car.make== currentNode.make and car.model==currentNode.model:
            currentNode.cars.append(car)
        
        else:
            if currentNode.right != None:
                self._addCar(car, currentNode.right)
            else:
                currentNode.right = CarInventoryNode(car)

    def doesCarExist(self, car):
        if self.root:
            res = self._doesCarExist(car, self.root)
            if res:
                return True
            else:
                return False
        else:
            return False

    def _doesCarExist(self, car, currentNode):
        if not currentNode:
            return False
        elif currentNode.make ==car.make and currentNode.model==car.model:
            for item in currentNode.cars:
                if item.year == car.year and item.price == car.price:
                    return True
        elif car.make < currentNode.make:
            return self._doesCarExist(car, currentNode.left)
        elif car.make==currentNode.make and car.model < currentNode.model:
            return self._doesCarExist(car, currentNode.left)
        else:
            return self._doesCarExist(car, currentNode.right)

    def inOrder(self):
        return self._inOrder(self.root)

    def _inOrder(self, currentNode):

        if currentNode==None:
            return ''
        leftresult = self._inOrder(currentNode.getLeft())
        current_result=''
        for car in currentNode.cars:
            current_result += str(car) + '\n'

        rightresult = self._inOrder(currentNode.getRight())

        return leftresult + current_result + rightresult

    def preOrder(self):
        return self._preOrder(self.root)

    def _preOrder(self, currentNode):

        if currentNode==None:
            return ''

        firstresult = ''
        for car in currentNode.cars:
            firstresult += str(car) + '\n'

        firstresult += self._preOrder(currentNode.getLeft())
        firstresult += self._preOrder(currentNode.getRight())
        return firstresult

    

    def getBestCar(self, make, model):
        
        if self.root:
            res = self._getBestCar(make, model, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _getBestCar(self, make, model, currentNode):
        if not currentNode:
            return None

        elif currentNode.make.upper()==make.upper() and currentNode.model.upper()==model.upper():
            bestCar= currentNode.cars[0]
            for car in currentNode.cars:
                if car.year > bestCar.year:
                    bestCar = car
                elif car.year==bestCar.year:
                    if car.price > bestCar.price:
                        bestCar = car
            return bestCar

        elif make< currentNode.make:
            return self._getBestCar(make, model, currentNode.getLeft())

        elif make==currentNode.make and model<currentNode.model:
            return self._getBestCar(make, model, currentNode.getLeft())
        else:
            return self._getBestCar(make, model, currentNode.getRight())


    def getWorstCar(self, make, model):
        
        if self.root:
            res = self._getWorstCar(make, model, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def _getWorstCar(self, make, model, currentNode):
        if not currentNode:
            return None

        elif currentNode.make.upper()==make.upper() and currentNode.model.upper()==model.upper():
            worstCar= currentNode.cars[0]
            for car in currentNode.cars:
                if car.year < worstCar.year:
                    worstCar = car
                elif car.year==worstCar.year:
                    if car.price < worstCar.price:
                        worstCar = car
            return worstCar

        elif make< currentNode.make:
            return self._getWorstCar(make, model, currentNode.getLeft())

        elif make==currentNode.make and model<currentNode.model:
            return self._getWorstCar(make, model, currentNode.getLeft())
        else:
            return self._getWorstCar(make, model, currentNode.getRight())


    def postOrder(self):
        return self._postOrder(self.root)

    def _postOrder(self, currentNode):

        if currentNode==None:
            return ''

        result= ''
        result += self._postOrder(currentNode.getLeft())
        result += self._postOrder(currentNode.getRight())

        for car in currentNode.cars:
            result += str(car) + '\n'
        return result
    
    def getTotalInventoryPrice(self):
        
        return self._getTotalInventoryPrice(self.root)

    def _getTotalInventoryPrice(self, currentNode):
        total = 0.0
        if currentNode==None:
            return 0

        total += self._getTotalInventoryPrice(currentNode.getLeft())
        total += self._getTotalInventoryPrice(currentNode.getRight())

        for car in currentNode.cars:
            total += car.price

        return total
            
            

    

    
        

        

car1 = Car("Dodge", "dart", 2015, 6000)
car2 = Car("dodge", "DaRt", 2003, 5000)
car2_5 = Car("dodge", "DaRt", 2015, 7000)
car3 = Car('Chevy', 'Volt', 2015, 15000)
car3_5 = Car('Chevy', 'Volt', 2018, 15000)
car4 = Car('Toyota', 'Prius', 2007, 6500)
car5 = Car('Toyota', 'Prius', 2007, 700)

inventory = CarInventory()
inventory.addCar(car1)
inventory.addCar(car2)
inventory.addCar(car3)
inventory.addCar(car4)
inventory.addCar(car5)
inventory.addCar(car2_5)
inventory.addCar(car3_5)



inventory.getBestCar('Dodge', 'Dart').price
inventory.getBestCar('Dodge', 'Dart').year
inventory.getBestCar('Toyota', 'Prius').price
inventory.getBestCar('Chevy', 'Volt').year

inventory.getWorstCar('Dodge', 'Dart').price
inventory.getWorstCar('Toyota', 'Prius').price

inventory.getTotalInventoryPrice()









    
            
        


    

        
            
 
