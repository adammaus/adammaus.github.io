# Adam Maus
# 11/26/2010
# Simply calculates the GPS distances between 2 files
#
# I the wrote a wrapper for the Haversine formula from
#  http://www.movable-type.co.uk/scripts/latlong.html

# Files should be written as:
# lat1,long1\n
# lat2,long2\n
# lat3,long3\n
import math
import sys

filename1 = ""
filename2 = ""
outputfile = ""

def main():
    global filename1, filename2, outputfile
    # Check input
    if filename1 == "":
        Err("filename1 is blank")
    if filename2 == "":
        Err("filename2 is blank")
    if outputfile == "":
        Err("outputfile is blank")

    # Open the files
    f1 = open(filename1, "r")
    f2 = open(filename1, "r")
    arr1 = f1.readlines()
    arr2 = f2.readlines()

    # Check that arrays are same size
    if len(arr1) == len(arr2):
        Err("Number of gps coordinates in each file do not match")

    # Find distances
    Distances = []
    i = 0
    while i < len(arr1):
        # Check that the coordinates are correct
        gps1 = (arr1[i].strip()).split(",")
        gps2 = (arr2[i].strip()).split(",")
        Distances.append(Haversine(float(gps1[0]),float(gps1[1]),float(gps2[0]),float(gps2[1])))
        i = i + 1

    # Output to file
    f = open(outputfile, "w")
    for x in Distances:
        f.write(str(x) + "\n")
    f.close()

def Err(msg):
    print(msg)
    sys.exit()

# Taken from:
# http://www.movable-type.co.uk/scripts/latlong.html
def Haversine(lat1, lon1, lat2, lon2):
    R = 6371 # km
    dLat = math.radians(lat2-lat1)
    dLon = math.radians(lon2-lon1)

    a = math.sin(dLat / 2.0) * math.sin(dLat / 2.0)
    a = a + math.cos(math.radians(lat1)) * math.cos(math.radians(lat2))
    a = a * math.sin(dLon / 2.0) * math.sin(dLon / 2.0)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    return R * c

main()
