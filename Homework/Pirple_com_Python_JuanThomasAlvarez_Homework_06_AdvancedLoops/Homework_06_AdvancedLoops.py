"""
Homework Assignment #6: Advanced Loops
*Done: Create a function that takes in two parameters: rows, and columns, both of which are integers. 
*Done: The function should then proceed to draw a playing board (as in the examples from the lectures) the same number of rows and columns as specified. 
*Done: After drawing the board, your function should return True.

Extra Credit:
*Done: Try to determine the maximum width and height that your terminal and screen can comfortably fit without wrapping. 
*Done: If someone passes a value greater than either maximum, your function should return False.
"""
import os #Library that enables us to query the size of the terminal
TerminalSize = os.get_terminal_size() #Saves the size of the terminal into a variable
MinimumColumnWidthAllowed = 15

def CreateTable(NumberOfRows,NumberOfColumns):
    global MinimumColumnWidthAllowed
    if(MinimumColumnWidthAllowed<10):
        MinimumColumnWidthAllowed = 10 #Override the minimum column width allowed if a value less than 5 is used int he global variable
    TableEachColumnWidth = int(TerminalSize.columns / NumberOfColumns)
    TableMaxWidthPossible = TableEachColumnWidth * NumberOfColumns

    if(NumberOfColumns > TerminalSize.columns/MinimumColumnWidthAllowed):
        print("Unable to Create a table with " + str(NumberOfColumns) + " columns because the Terminal is too small and the minimum table column width allowed is " + str(MinimumColumnWidthAllowed) + " terminal columns.")
        TablePrinted = False
        return TablePrinted
    else:
        TablePrinted = True
    

    print("-"*TableMaxWidthPossible)
    for TableRow in range(NumberOfRows*2): #Duplicate the number of rows sent to function to represent Table rows instead of Terminal Rows.
        if TableRow%2 == 0: #0,2,4
            for TableColumn in range(1,TableMaxWidthPossible + 1): #1,2,3,4,5,etc.
                if TableColumn%TableEachColumnWidth != 1:
                    if TableColumn != TableMaxWidthPossible:
                        print(" ",end="")
                    else:
                        print("|")
                else:
                    print("|",end="")
        else:
            print("-"*TableMaxWidthPossible)
    return TablePrinted

print("")
print("Printing a 1 column table with 4 rows")
CreateTable(4,1)
print("")
print("Printing a 2 column table with 4 rows")
CreateTable(4,2)
print("")
print("Printing a 3 column table with 4 rows")
CreateTable(4,3)
print("")
print("Printing a 4 column table with 4 rows")
CreateTable(4,4)
print("")
print("Printing a 9 column table with 4 rows")
CreateTable(4,9)
print("")
print("Printing a 200 column table with 4 rows which will fail")
CreateTable(4,200)
print("")