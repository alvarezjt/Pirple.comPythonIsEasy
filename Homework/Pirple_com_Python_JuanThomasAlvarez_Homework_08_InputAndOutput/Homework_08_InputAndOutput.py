"""Homework Assignment #8: Input and Output (I/O)
*Done: Create a note-taking program. When a user starts it up, it should prompt them for a filename.
*Done: If they enter a file name that doesn't exist, it should prompt them to enter the text they want to write to the file. After they enter the text, it should save the file and exit.
*Done: If they enter a file name that already exists, it should ask the user if they want:
*Done: A) Read the file
*Done: B) Delete the file and start over
*Done: C) Append the file
*Done: If the user wants to read the file it should simply show the contents of the file on the screen. 
*Done: If the user wants to start over then the file should be deleted and another empty one made in its place. 
*Done: If a user elects to append the file, then they should be able to enter more text, and that text should be added to the existing text in the file. 
Extra Credit:
*Done: Allow the user to select a 4th option:
*Done: D) Replace a single line
*Done: If the user wants to replace a single line in the file, they will then need to be prompted for 2 bits of information:
*Done: 1) The line number they want to update.
*Done: 2) The text that should replace that line.
"""
import os
varFilename = input("Let's create a new note, what name do you want to give your file?\nFilename: ")
varFileExists = os.path.exists(varFilename)

if varFileExists:
    varFileAction = input("This file already  exists... What do you wish to do with this file?\nA) Read the file\nB) Delete the file and start over\nC) Append the file\nD) Replace a single line\n")
    if varFileAction == "a": #Reading the file.
        print("Reading the file:")
        varFile = open(varFilename,"r")
        print("The file now has the following content:\n"+varFile.read())
        varFile.close()
    elif varFileAction == "b": #Deleting and starting over.
        print("Deleting the file and starting over:")
        os.remove(varFilename)
        varFile = open(varFilename,"w")
        varFile.write(input())
        varFile.close()
        varFile = open(varFilename,"r")
        print("The file now has the following content:\n"+varFile.read())
        varFile.close()
    elif varFileAction == "c": #Appending to the file.
        print("Appending to the file:")
        varFile = open(varFilename,"a")
        varFile.write(input())
        varFile.close()
        varFile = open(varFilename,"r")
        print("The file now has the following content:\n"+varFile.read())
        varFile.close()
    elif varFileAction == "d": #Replace a single line
        varFileByLine = []
        varFile = open(varFilename,"r+")
        for line in varFile:
            varFileByLine.append(line)
        varFile.close()
        print("Replacing a single line in the file:")
        varLineToUpdate = int(input("There are "+str(len(varFileByLine))+" line(s) of text in this file, which line of text do you wish to update?\n"))
        varNewLine = input("Please enter your new line of text:\n")
        if varLineToUpdate <= len(varFileByLine):
            if varLineToUpdate == len(varFileByLine):
                varFileByLine[varLineToUpdate-1] = varNewLine
            else:
                varFileByLine[varLineToUpdate-1] = varNewLine + "\n"
            os.remove(varFilename)
            varFile = open(varFilename,"w")
            varFile.writelines(varFileByLine)
            varFile.close()
    else:
        print("You have not selected an action, terminating the program.")

else:
    varFile = open(varFilename,"w")
    varFile.write(input("Please enter your note below:\n"))
    varFile.close()