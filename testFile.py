from CarInventory import CarInventory
from Car import Car
from CarInventoryNode import CarInventoryNode

car1 = Car("Dodge", "dart", 2015, 6000)
car2 = Car("dodge", "DaRt", 2003, 5000)
car3 = Car('Chevy', 'Volt', 2015, 15000)
car4 = Car('Toyota', 'Prius', 2007, 6500)
car0 = Car('Honda', '4runner', 2007, 6500)
car5 = Car('Toyota', 'Prius', 2007, 700)

inventory = CarInventory()
inventory.addCar(car1)
inventory.addCar(car2)
inventory.addCar(car3)
inventory.addCar(car4)

carNode = CarInventoryNode(car1)
carNode.cars.append(car2)
carNode.setRight(car3)

def test_inOrder():
    assert inventory.inOrder()=='Make: CHEVY, Model: VOLT, Year: 2015, Price: $15000\nMake: DODGE, Model: DART, Year: 2015, Price: $6000\nMake: DODGE, Model: DART, Year: 2003, Price: $5000\nMake: TOYOTA, Model: PRIUS, Year: 2007, Price: $6500\n'

    
def test_preOrder():
    assert inventory.preOrder()=='Make: DODGE, Model: DART, Year: 2015, Price: $6000\nMake: DODGE, Model: DART, Year: 2003, Price: $5000\nMake: CHEVY, Model: VOLT, Year: 2015, Price: $15000\nMake: TOYOTA, Model: PRIUS, Year: 2007, Price: $6500\n'

def test_postOrder():
    assert inventory.postOrder()=='Make: CHEVY, Model: VOLT, Year: 2015, Price: $15000\nMake: TOYOTA, Model: PRIUS, Year: 2007, Price: $6500\nMake: DODGE, Model: DART, Year: 2015, Price: $6000\nMake: DODGE, Model: DART, Year: 2003, Price: $5000\n'

def test_doesCarExist():
    assert inventory.doesCarExist(car1)==True
    assert inventory.doesCarExist(car2)==True
    assert inventory.doesCarExist(car0)==False

def test_getMake():
    assert carNode.getMake()=='DODGE'

def test_getRight():
    assert carNode.getRight().make == 'CHEVY'

def test_getBestCar():   
    assert inventory.getBestCar('Dodge', 'Dart').price==6000
    assert inventory.getBestCar('Dodge', 'Dart').year==2015
    assert inventory.getBestCar('Toyota', 'Prius').price==6500
    
    
    
def test_getWorstCar():
    assert inventory.getWorstCar('Dodge', 'Dart').price==5000
    assert inventory.getWorstCar('Toyota', 'Prius').price==6500


    
    
    
    
