import json
import os
import requests
import time
from geopy.geocoders import Nominatim
from geopy.adapters import AioHTTPAdapter


#Api's url

persones = "http://api.open-notify.org/astros.json"

location2  = "http://api.open-notify.org/iss-now.json"


#function
def message():
    print("Welcome to this little program, just figuring out how to use api's.\nSometimes you just can't get the exact adress of the ISS.\nThe comands for this program are:\n-people \n-location\n-clear\n-exit\nEnjoy!\n")
    print("---------------------------------------------------------------------------------")
    print("Press enter to continue:")
    input()
    os.system('cls||clear')
    print("Comands: \n-people \n-location\n-clear\n-exit")


#Get the people that are currently in the ISS
def func_people():
    r = requests.get(persones)
    if (not r.ok):
        print("Error: Couldn't connect to ISS Data")
        quit()
    dades = r.json()
    print("These are the people currently on the ISS: \n")
    for x in dades["people"]:
        print(x["name"])
    print("\n")
    
#Get the position of the ISS
def func_location():
    print("The location of the ISS is: ")
    r = requests.get(location2)
    if (not r.ok):
        print("Error: Couldn't connect to ISS Data")
        quit()
    dades = r.json()
    latitude = dades["iss_position"]["latitude"]
    longitude = dades["iss_position"]["longitude"]
    print("   Latitude: {}\n   Longitude: {}\n".format(latitude,longitude))

    print("The exact location is:\n")
    geolocator = Nominatim(user_agent="prova_ISS")
    coordinates = latitude + ', ' + longitude
    location = geolocator.reverse(coordinates,language = 'es')
    if (not location):
        print("Error: Couldn't get the exact adress, the ISS might be over the sea. Try later.\n")
    else:
        print(location.address)



#Main function
message()

while True:
    a = input();
    print("\n")
    if (a == "exit"):
        print("Do you want to keep the information in the terminal? y/N")
        res = input()
        if (res != 'y'):
            os.system('cls||clear')
        break
    elif(a == "clear"):
        os.system('cls||clear')
        print("Comands: \n-people \n-location\n-clear\n-exit\n")
    elif(a == "people"):
        func_people()
    elif(a == "location"):
        func_location()
