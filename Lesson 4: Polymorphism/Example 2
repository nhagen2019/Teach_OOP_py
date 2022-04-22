#creates the car class
class Car:
    #defines the variables for name and color and links them to car
    def __init__(item, name, color):
        item.name = name
        item.color = color
    
    #defines the car type function
    def type(item):
        print(f"I am a {item.color} {item.name}")

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

    #defines the train speed function
    def speed(item):
       print("Since I am a train I can travel between 0 - 500 MPH")

car1 = Car("Corvette", "Black")
car2 = Car("Ferrari", "Red")

train1 = Train("Steam Engine", "Yellow")

for vehicle in (car1, car2, train1):
    vehicle.type()
    vehicle.speed()
