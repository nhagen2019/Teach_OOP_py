from cgi import test
import unittest

#creates the car class
class Car:
    #defines the variables for name and color and links them to car
    def __init__(item, name, color):
        item.name = name
        item.color = color
    
    #defines the car type function
    def type(item):
        print(f"I am a {item.color} {item.name}")
        return item.color,item.name

    #defines the car speed function
    def speed(item):
        print("Since I am a car I can travel between 0 - 200 MPH")

#creates the train class
class Train:
    #defines the variables for name and color and links them to the train
    def __init__(item, name, color):
        item.name = name
        item.color = color

    #defines the train type function
    def type(item):
        print(f"I am a {item.color} {item.name}")
        return item.color,item.name

    #defines the train speed function
    def speed(item):
       print("Since I am a train I can travel between 0 - 500 MPH")

def test1():
    print("Test 1:")
    car1 = Car("Car1", "Color1")
    car2 = Car("Car2", "Color2")

    train1 = Train("Train1", "Color3")

    i = 0
    testcases = [("Color1", "Car1"), ("Color2", "Car2"), ("Color3", "Train1",)]
    flag = True
    for vehicle in (car1, car2, train1):
        a,b = vehicle.type()
        c = vehicle.speed()
        #print(a)
        #print(b)
        #print(testcases[i])
        #print((a,b))
        if(testcases[i] != (a,b)):
            flag = False
        i = i + 1
    
    if(flag == True):
        print("Pass")
    else:
        print("Fail")
    
def test2():
    print("Test 2:")
    car1 = Car("Semi Truck", "Yellow")
    car2 = Car("Camry", "Orange")

    train1 = Train("Bullet Train", "Black")

    i = 0
    testcases = [("Yellow", "Semi Truck"), ("Orange", "Camry"), ("Black", "Bullet Train",)]
    flag = True
    for vehicle in (car1, car2, train1):
        a,b = vehicle.type()
        c = vehicle.speed()
        #print(a)
        #print(b)
        #print(testcases[i])
        #print((a,b))
        if(testcases[i] != (a,b)):
            flag = False
        i = i + 1
    
    if(flag == True):
        print("Pass")
    else:
        print("Fail")

def test3():
    print("Test 3:")
    car1 = Car("Elantra", "Black")
    car2 = Car("Expedition", "White")

    train1 = Train("Freight Train", "Orange")

    i = 0
    testcases = [("Black", "Elantra"), ("White", "Expedition"), ("Orange", "Freight Train",)]
    flag = True
    for vehicle in (car1, car2, train1):
        a,b = vehicle.type()
        c = vehicle.speed()
        #print(a)
        #print(b)
        #print(testcases[i])
        #print((a,b))
        if(testcases[i] != (a,b)):
            flag = False
        i = i + 1
    
    if(flag == True):
        print("Pass")
    else:
        print("Fail")

test1()
print("\n")
test2()
print("\n")
test3()
