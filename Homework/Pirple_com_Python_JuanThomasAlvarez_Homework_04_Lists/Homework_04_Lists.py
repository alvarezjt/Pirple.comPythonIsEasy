"""
Homework Assignment #4: Lists
1. Create a global variable called myUniqueList. It should be an empty list to start.
2. Next, create a function that allows you to add things to that list. 
    2.1 Anything that's passed to this function should get added to myUniqueList, unless its value already exists in myUniqueList. 
        2.1.1 If the value doesn't exist already, it should be added and the function should return True. 
        2.1.2 If the value does exist, it should not be added, and the function should return False;
3. Finally, add some code below your function that tests it out. 
    3.1 It should add a few different elements, showcasing the different scenarios,
    3.2 and then finally it should print the value of myUniqueList to show that it worked.

Extra Credit:
Add another function that pushes all the rejected inputs into a separate global array called myLeftovers. 
If someone tries to add a value to myUniqueList but it's rejected (for non-uniqueness), it should get added to myLeftovers instead.
"""

myUniqueList=[] #Declare a global variable of unique values.
myLeftOvers=[] #Declare global variable to hold items rejected by myUniqueList.
myLeftOversAutoIncrement = 0

def AddItemToMyUniqueList(LastName,FirstName):
    LocalList = [LastName,FirstName]
    if(LocalList in myUniqueList):
        print(LocalList)
        print(LocalList[1] + " " +LocalList[0] + " already exists in myUniqueList, and has been rejected.  To view all rejected items, please see myLeftOvers.")
        AddItemToMyLeftOvers(LocalList)
        ResultToReturn = False
    else:
        myUniqueList.append(LocalList)
        print(LocalList)
        print(LocalList[1] + " " +LocalList[0] + " has been appended to myUniqueList.")
        ResultToReturn = True
    return ResultToReturn


def AddItemToMyLeftOvers(ListRejected):
    global myLeftOversAutoIncrement
    ListRejected.append(myLeftOversAutoIncrement)
    myLeftOvers.append(ListRejected)
    myLeftOversAutoIncrement += 1


print(AddItemToMyUniqueList("Doe","John"))
print(AddItemToMyUniqueList("Doe","John"))
print(AddItemToMyUniqueList("Doe","John"))
print(AddItemToMyUniqueList("Dion","Celine"))
print(AddItemToMyUniqueList("Norwood","Brandy"))
print(AddItemToMyUniqueList("Jerkins","Rodney"))
print(AddItemToMyUniqueList("Jerkins","Rodney"))
print("")
print("myUniqueList:")
print(myUniqueList)
print("")
print("myLeftOvers:")
print(myLeftOvers)
