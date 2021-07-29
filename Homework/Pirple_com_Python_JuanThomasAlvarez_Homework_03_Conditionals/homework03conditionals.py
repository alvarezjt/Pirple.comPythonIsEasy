"""
Create a function that accepts 3 parameters and checks for equality between any two of them.
Your function should return True if 2 or more of the parameters are equal, and false is none of them are equal to any of the others.
Extra Credit:
Modify your function so that strings can be compared to integers if they are equivalent. For example, if the following values are passed to your function: 6,5,"5"
You should modify it so that it returns true instead of false.
"""

def CompareThree(Param1,Param2,Param3):
    if int(Param1) == int(Param2) or int(Param1) == int(Param3) or int(Param2) == int(Param3):
        ComparisonResult = True
    else:
        ComparisonResult = False
    return ComparisonResult

print(CompareThree(6,5,"5"))