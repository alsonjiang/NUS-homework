#Dog is a class, class names are written in PascalCase convention
class Dog:
    #class attributes. All class instances have the same value
    species = "Canis familiaris"
    
    #init initialises each new instances of the class, gives every new Dog object initial state
    def __init__(self,name,age): #first variable always == "self"
        #init is an example of Dunder(double underscore) functions
        self.name = name
        self.age = age
        #instance attributes. All Dog objects will have name,age. But each instance will have different values of name,age

    #instance methods
    #basically a function that only can be called in an instance of Dog() class
    #it is useful to have a method that returns useful info. of the class!
    def __str__(self):
        return f"{self.name} is {self.age} years old."
        #f strings to insert variables into strings 

    def speak(self,sound):
        return f"{self.name} says {sound}"
        
        
miles = Dog("Miles",4)
#instantiating a Dog instance called miles
#must give positional arguments based on the instance attributes
#will be saved in a unique memory address

#print(miles.name)
#prints "Miles"
#access instance attribute using dot notation

miles.species = "Felis silvestris"
#changing class attributes dynamically
#instance miles will have a different species attribute

#print(miles.speak("woof woof"))
#example of using an instance method

#print(miles)
#using __str__ to show information of the attributes - the Pythonic way.


#test my knowledge
class Car:

    def __init__(self,colour=str, mileage=int):
        self.colour = colour
        self.mileage = mileage

blue_car = Car("blue",1000)



