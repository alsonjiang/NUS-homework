#OOP OOP OOP 

#part 1: bank accounts
class BankAccount():
    #constructor, class atttibutes
    def __init__(self,name, balance, interest_rate):
        self.name = name
        self.balance = balance
        self.interest_rate = interest_rate
        self.giro = 0
    
    #class methods
    def withdraw(self, name, amount):
        if name != self.name:
            print("You are not authorized for this account")
        else:
            if self.balance < amount:
                print(f"Money not enough! You do not have ${amount}")
                return 0
            else:
                self.balance -= amount
                return amount
        
    def showBalance(self):
        print(f'Your balance is ${self.balance}')

    def deposit(self, amount):
        self.balance += amount
    
    def oneYearHasPassed(self):
        if self.giro == 0: #no giro to be deducted
            self.balance += self.balance * self.interest_rate
        else:
            self.balance -= self.giro
            self.balance += self.balance * self.interest_rate

    def transferTo(self, account, amount):
        if self.balance >= amount:
            self.balance -= amount
            account.balance += amount
            print(f"You have transferred {amount} to {account}")
            return self.showBalance()
        else:
            print("You do not have enough to make the transfer")
            return self.showBalance()
    
    def setUpGiro(self, amount):
        self.giro = amount


class MinimalAccount(BankAccount):
    def __init__(self, name, balance, interest_rate):
        super().__init__(name, balance, interest_rate)
    
    def oneYearHasPassed(self):
        if self.balance < 1000:
            if (self.balance - 20) >= 0:
                self.balance -= 20
            else:
                self.balance = 0

        return super().oneYearHasPassed()
    

class JointAccount(BankAccount):
    def __init__(self, name, name2, balance, interest_rate):
        super().__init__(name, balance, interest_rate)
        self.name2 = name2 #new attribute local to this class
    
    def withdraw(self, current_name, amount):
        #check if entered name equals to either of the pre-set names
        if (current_name != self.name) and (current_name != self.name2): 
            print("You are not authorized for this account")
        else:
            if self.balance < amount:
                print(f"Money not enough! You do not have ${amount}")
                return 0
            else:
                self.balance -= amount
                return amount


#part 2: vehicles

class Cannon:
    def __init__(self):
        self.numAmmo = 0
    def fire(self):
        if self.numAmmo:
            print("Fire!!!!!!!")
            self.numAmmo -= 1
        else:
            print("No more ammo")
    def reload(self):
        if self.numAmmo:
            print("Unable to reload")
        else:
            print("Cannon reloaded")
            self.numAmmo += 1

class Vehicle:
    def __init__(self,pos):
        self.pos = pos
        self.velocity = (0,0)
        self.petrol = 0

    def setVelocity(self,vx,vy):
        self.velocity = (vx,vy)

    def move(self): #1 call of move() = move 1 time
        if self.petrol >= 1:
            self.pos = (self.pos[0]+self.velocity[0],self.pos[1]+self.velocity[1])
            self.petrol -= 1
            print(f"Move to {self.pos}")    
        else: 
            print("Out of petrol. Cannot Move")

    def addPetrol(self, liters):
        self.petrol += liters

class Tank(Vehicle,Cannon):
    def __init__(self,pos):
        Vehicle.__init__(self,pos)
        Cannon.__init__(self)
        
class Sportscar(Vehicle):
    def turnOnTurbo(self):
        print("VROOOOOOOM......")
        self.velocity = (self.velocity[0]*2,self.velocity[1]*2)
        print(f"Velocity increased to {self.velocity}")

class Lorry(Vehicle):
    def __init__(self,pos):
        super().__init__(pos)  
        self.cargo = [] 
    def load(self,cargo):
        self.cargo.append(cargo)
    def unload(self,cargo):
        if cargo in self.cargo:
            self.cargo.remove(cargo)
            print(f"Cargo {cargo} unloaded.")
        else:
            print(f"Cargo {cargo} not found.")
    def inventory(self):
        print("Inventory:"+str(self.cargo))

class Bisarca(Lorry):
    def __convertCargo(self):
        output = []
        for c in self.cargo:
            output.append(str(type(c)).split('.')[1].split('\'')[0])
        return output
    def inventory(self):
        print("Inventory:"+str(self.__convertCargo()))            
    def load(self,cargo):
        if isinstance(cargo,Vehicle):
            super().load(cargo)
        else:
            print(f'Your cargo ({cargo}) is not a vehicle!')

class BattleBisarca(Bisarca,Cannon):
    def __init__(self,pos):
        Bisarca.__init__(self,pos)
        Cannon.__init__(self)

'''
OptimasPrime = BattleBisarca((0,0))
OptimasPrime.load("Food")
                  
myCar = Sportscar((0,0))
myCar.setVelocity(0,40)
myCar.move()
myCar.turnOnTurbo()
myCar.move()


myTruck = Lorry((10,10))
myTruck.setVelocity(10,0)
myTruck.move()
myTruck.load("Food")
myTruck.load("Supplies")
myTruck.inventory()
myTruck.unload("Food")
myTruck.inventory()
myTruck.unload("Gold")

myDadTruck = Bisarca((0,0))
myDadTruck.load("Food")
myDadTruck.load(myCar)
myDadTruck.load(myTruck)
myDadTruck.inventory()
    
'''
