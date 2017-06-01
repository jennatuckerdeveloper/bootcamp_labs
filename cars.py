class Car:
    def __init__(self, color, number_of_doors):
        number_of_wheels = 4
        self.color = color
        self.number_of_doors = number_of_doors
    def __str__(self):
    #overloads the print function
        return "A {}, {} - door Honda".format(self.color, self.number_of_doors)
    def honk():
        print("Honk!")
