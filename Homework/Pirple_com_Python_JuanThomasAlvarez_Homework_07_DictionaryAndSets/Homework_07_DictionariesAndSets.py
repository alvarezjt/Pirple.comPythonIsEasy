"""
Homework Assignment #7: Dictionaries and Sets
*Done: Return to your first homework assignments, when you described your favorite song. Refactor that code so all the variables are held as dictionary keys and value. 
*Done: Then refactor your print statements so that it's a single loop that passes through each item in the dictionary and prints out it's key and then it's value.

Extra Credit:
*Done: Create a function that allows someone to guess the value of any key in the dictionary, and find out if they were right or wrong. 
*Done: This function should accept two parameters: Key and Value. If the key exists in the dictionary and that value is the correct value, then the function should return true. 
*Done: In all other cases, it should return false.
"""

FavoriteSongDictionarySet = {"Song":"The Hard Way","Duration":"0.0023611111111111","BPM":"120","Album":"Courage (Deluxe Edition)","YearReleased":"2019","Artist":"Celine Dion","Genre":"World"}

for SongCriteria in FavoriteSongDictionarySet:
    print(SongCriteria + ": " + str(FavoriteSongDictionarySet[SongCriteria]))

def SongSearch(SearchCriteria,SearchValue):
    global FavoriteSongDictionarySet
    if FavoriteSongDictionarySet[SearchCriteria] == SearchValue:
        return True
    else:
        return False

while(True):
    UserSearchCriteria = str(input("Please enter the song criteria. Are you searching by Song, Artist, Album, Duration, BPM, YearReleased or Genre?\n"))
    UserSearchValue = str(input("Please enter the "+ str(UserSearchCriteria) + "\n"))
    if SongSearch(UserSearchCriteria,UserSearchValue):
        print("The search for " + str(UserSearchValue) + " in the criteria " + str(UserSearchCriteria) + " was found.")
    else:
        print("No match found for " + str(UserSearchValue) + " in the criteria " + str(UserSearchCriteria))