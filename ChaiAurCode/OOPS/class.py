# Object Oriented Programming Basic classes & object ;
# Create a car class with attributes like brand and model.Then create an instance of this class.
# Add a method to the car class that displays the full nam eof the car (brand and model) ;
# Display Inheritence by building an Electric car class that inherits from the Car class and has an additional  attribute battery_size;
# Encapsulation : Modify the car class to encapsulate the brand attribute , making it private , and provide a getter method for it  ;
# Add a class variable to Car that keeps the track of the number of cars created ;
# Static  methods : Add a static method to the car class that returns a general description of a car ;
# Demonstrate the use of isinstance() to check if my_tesla is an instance of Car and ElectricCar ; 
# Create two classes Battery and Engine , and let the ElectricCar class inherit from both , demonstrating multiple inheritence ;

class Car :
    total_car = 0
    def __init__(self,brand,model):         # behaves like constructor;
        self.__brand = brand
        self.__model = model                # making a variable private by putting ( __ )before the variable ;
        Car.total_car += 1

    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model


    def fullName(self):
        return f"{self.get_brand()} {self.get_model()}"
    
    @staticmethod                          #Decorators
    def general_description():             # no need to give [self] as no objects need to accces it
        return "Cars are means of the transport..!!"
    
class ElectricCar(Car):
    def __init__(self ,brand,model,battery_size):
        super().__init__(brand,model)                # Accessing the property from parent
        self.battery_size = battery_size

    def fullName(self):
        return f"{self.get_brand()} {self.get_model()} {self.battery_size}"

class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is Engine"
    
class ElectricCarTwo(Battery ,Engine,Car):
    pass


obj = Car("Honda" , "City")
print(obj.get_brand())
print(obj.get_model())
print(obj.fullName())

my_car = Car("TATA" ,"Safari")
print(my_car.get_brand())
print(my_car.get_model())
print(my_car.fullName())
# print(my_car.general_description())       # not working when made static method ;
print(Car.general_description())          #working when made static method ;


tesla = ElectricCar("Tesla" ,"ModelS","80 Kwh")
print(tesla.battery_size)
print(tesla.fullName())

# To print the nuber of objects is created for the class by checking on the constructer called ;
print(Car.total_car)

# to check if the method is the instance of the respective class or not ;
print(isinstance(my_car ,Car))                       #True
print(isinstance(tesla ,ElectricCar))                #True

new_car = ElectricCarTwo("Tesla" , "spaceX")
print(new_car.engine_info())
print(new_car.battery_info())