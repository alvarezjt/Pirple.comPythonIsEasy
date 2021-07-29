"""
Celine is KING v.1.0.001
Programmer: Juan Thomas Alvarez
Copyrights Celine Dion, 2019.

General Information:
Program shows my favorite song. FYI It isn't really my favorite, I was just listening to it at the time.
"""

import math #Making math functions available to program from a standard math library.

Song="The Hard Way" #Name of the song.
Duration=0.0023958333333333 #time where 24 hours = 1.
BPM=120 #Beats Per Minute (This value was made up).
Album="Courage (Deluxe Edition)" #The album the song was first released on.
YearReleased="2019" #Year the song was released.
Artist="Celine Dion" #The artist's recognized commercial name
Genre="World" #The main genre for artist, not the song.

"""
Song Duration function will convert the decimal value into friendly human readable text.
Seconds will only print if song duration isn't a complete minute.
"""
def SongDuration(DurationInDecimal):
    oneminute = ((1/24)/60) #Calculates value of one minute in decimal
    onesecond = oneminute/60 #Calculates value of one second in decimal
    DurationSeconds = round((DurationInDecimal % oneminute)/onesecond) #Calculates how many seconds the song lasts for after the last minute passes.
    DurationMinutes = math.floor(DurationInDecimal / oneminute) #Calculates minutes completed in song duration
    PrintSeconds = False #Boolean for deciding weather or not to include seconds in result.
    if (DurationSeconds > 0):
        PrintSeconds = True
    else:
         PrintSeconds = False
    SongDurationResult = str(DurationMinutes) +" minutes"
    if (PrintSeconds): 
        SongDurationResult += " and " + str(DurationSeconds) + " seconds." 
    else:
        SongDuration += "."
    return SongDurationResult

#Function for Song Beats Per Minute simply adds a descriptive string at the end of the value.
def SongBPM(BeatsPerMinute):
    SongBPMResult = str(BeatsPerMinute) + " beats per minute."
    return SongBPMResult

def FormatYearReleased(Year):
    return "Year: " + Year


#Function returns boolean which is used to decide printed message.
def ReleasedThisYear(Year):
    if (int(Year) == "2021"):
        IsThisYear = True
    else:
        IsThisYear = False
    return IsThisYear

FavSinger = "Celine Dion"

if FavSinger == "Justin Timberlake":
    print("Your favorite singer is Justin Timberlake.")
elif FavSinger == "Celine Dion":
    print("Your favorite singer is Celine Dion.")
else:
    print("You do not have a favorite singer.")

#Print out each detail of favorite song on a new line
print(Song)
print(SongDuration(Duration))
print(SongBPM(BPM))
print(Album)
print(FormatYearReleased(YearReleased))
print(Artist)
print(Genre)
if (ReleasedThisYear(YearReleased)):
    print("Released this year.")
else:
    print("Not released this year.")