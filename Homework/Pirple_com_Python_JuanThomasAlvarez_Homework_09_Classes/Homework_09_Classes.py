""" Homework Assignment #9: Classes
Details:
*Done: Create a class called "Vehicle" and methods that allow you to set the "Make", "Model", "Year,", and "Weight".
*Done: The class should also contain a "NeedsMaintenance" boolean that defaults to False, and and "TripsSinceMaintenance" Integer that defaults to 0.
*Done: Next an inheritance classes from Vehicle called "Cars".
*Done: The Cars class should contain a method called "Drive" that sets the state of a boolean isDriving to True.  
*Done: It should have another method called "Stop" that sets the value of isDriving to false.
*Done: Switching isDriving from true to false should increment the "TripsSinceMaintenance" counter. 
*Done: And when TripsSinceMaintenance exceeds 100, then the NeedsMaintenance boolean should be set to true.
*Done: Add a "Repair" method to either class that resets the TripsSinceMaintenance to zero, and NeedsMaintenance to false.
*Done: Create 3 different cars, using your Cars class, and drive them all a different number of times. 
*Done: Then print out their values for Make, Model, Year, Weight, NeedsMaintenance, and TripsSinceMaintenance
Extra Credit: 
*Done: Create a Planes class that is also an inheritance class from Vehicle. 
*Done: Add methods to the Planes class for Flying and Landing (similar to Driving and Stopping), but different in one respect: 
*Done: Once the NeedsMaintenance boolean gets set to true, any attempt at flight should be rejected (return false), 
*Done: and an error message should be printed saying that the plane can't fly until it's repaired.
"""

class Vehicle():
    def __init__(self,Make="Undefined",Model="Undefined",Year="Undefined",Weight="Undefined"):
        self.Make = Make
        self.Model = Model
        self.Year = Year
        self.Weight = Weight
        self.NeedsMaintenance = False
        self.TripsSinceMaintenance = 0
    
    def setMake(self,Make):
        self.Make = Make
    
    def setModel(self,Model):
        self.Model = Model
    
    def setYear(self,Year):
        self.Year = Year
    
    def setWeight(self,Weight):
        self.Weight = Weight
    
class Cars(Vehicle):
    def __init__(self,Make="Undefined",Model="Undefined",Year="Undefined",Weight="Undefined"):
        Vehicle.__init__(self,Make,Model,Year,Weight)
        self.isDriving = False

    def Drive(self):
        self.isDriving = True

    def Stop(self):
        if (self.isDriving == True):
            self.isDriving = False
            self.TripsSinceMaintenance += 1
            if (self.TripsSinceMaintenance > 100):
                self.NeedsMaintenance = True

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

    def __str__(self):
        return  "Make: " + self.Make + "   Model: " +  self.Model + "   Year: " +  self.Year + "   Weight: " +  self.Weight + "   NeedsMaintenance: " +  str(self.NeedsMaintenance) + "   TripsSinceMaintenance: " +  str(self.TripsSinceMaintenance)

class Planes(Vehicle):
    def __init__(self,Make="Undefined",Model="Undefined",Year="Undefined",Weight="Undefined"):
        Vehicle.__init__(self,Make,Model,Year,Weight)
        self.isDriving = False

    def Flying(self):
        if (self.NeedsMaintenance != True):
            self.isDriving = True
        else:
            self.isDriving = False
            print("The plane can't fly until it's repaired.")
            return False

    def Landing(self):
        if (self.isDriving == True):
            self.isDriving = False
            self.TripsSinceMaintenance += 1
            if (self.TripsSinceMaintenance > 100):
                self.NeedsMaintenance = True

    def Repair(self):
        self.TripsSinceMaintenance = 0
        self.NeedsMaintenance = False

    def __str__(self):
        return  "Make: " + self.Make + "   Model: " +  self.Model + "   Year: " +  self.Year + "   Weight: " +  self.Weight + "   NeedsMaintenance: " +  str(self.NeedsMaintenance) + "   TripsSinceMaintenance: " +  str(self.TripsSinceMaintenance)

CarOne = Cars("Honda","Civic","2020","3000")
CarTwo = Cars("Mazda","CX-5","2022","3554")
CarThree = Cars("Nissan","Kicks","2022","3485")
PlaneOne = Planes("Boeing","747","2022","120000")

for i in range(101):
    CarOne.Drive()
    CarOne.Stop()

for i2 in range(85):
    CarTwo.Drive()
    CarTwo.Stop()

for i3 in range(128):
    CarThree.Drive()
    CarThree.Stop()

for i3 in range(105):
    PlaneOne.Flying()
    PlaneOne.Landing()

print(CarOne)
print(CarTwo)
print(CarThree)
print(PlaneOne)