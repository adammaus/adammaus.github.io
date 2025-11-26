---
layout: post
title: GPS Distances
date: 2011-03-13T21:24:18-05:00
excerpt: A wrapper program that calculates distances from GPS coordinates in two files.
permalink: 2011/03/gps-distances/
tags:
  - Python
---
A wrapper program that calculates distances from GPS coordinates in two files.

{% highlight python %}
# Simply calculates the GPS distances between 2 files
#
# A wrapper for the Haversine formula from http://www.movable-type.co.uk/scripts/latlong.html
#
# Files could be written as:
# lat1,long1\n
# lat2,long2\n
# lat3,long3\n
import math
import sys
import csv

# Configuration
filename1 = "Test.csv"

# FileName1's id field, leave at -1 for line number
IDs1 = 0

# What columns the Coords are in
Coords1 = {"lat":1, "lon": 2} # Used lon since LONG may be a reserved word in different languages
filename2 = ""         # If filename2 is blank, we will look at filename1's contents

# If FileName is specified, fileName2's id field, leave at -1 for line number
IDs2 = -1
Coords2 = {"lat":1, "lon": 2}

# CSV Properties
Delimiter = ',' # Delimiter between csv
QuoteChar = '"' # How Quotes are done in the csv file

# Output file name
# Output distance is in miles
outputfile = "Test1.csv"

def main():
    global filename1, filename2, Delimiter, QuoteChar
    # Check input
    CheckSelf = False
    if filename1 == "":
        Err("filename1 is blank")
    if filename2 == "":
        print("Comparing all of filename1's contents to itself")
        CheckSelf = True
    if outputfile == "":
        Err("outputfile is blank")

    if CheckSelf:
        f1Name = filename1
        f2Name = filename1

        # Open the files
        f1 = csv.reader(open(f1Name, "rb"), delimiter=Delimiter, quotechar=QuoteChar)
        arr1 = []
        arr2 = []
        for row in f1:
            arr2.append(row)

        LengthOfFile1 = len(arr2)
        # Compare the file contents to itself
        i = 0
        while i < LengthOfFile1:
            arr1.append(arr2[0])
            i = i + 1
        i = 1
        while i < LengthOfFile1:
            j = i
            while j < LengthOfFile1:
                arr1.append(arr2[i])
                arr2.append(arr2[j])
                j = j + 1
            i = i + 1
    else:
        f1Name = filename1
        f2Name = filename2

        # Open the files
        f1 = csv.reader(open(f1Name, "rb"), delimiter=Delimiter, quotechar=QuoteChar)
        f2 = csv.reader(open(f2Name, "rb"), delimiter=Delimiter, quotechar=QuoteChar)
        arr1 = []
        arr2 = []
        for row in f1:
            arr1.append(row)
        for row in f2:
            arr2.append(row)

    # Check that arrays are same size
    if len(arr1) != len(arr2):
        Err("Number of gps coordinates in each file do not match")
    print("Number of Distances: " + str(len(arr1)))
    [ID1, ID2, Distances] = CalculateArrayDistances(arr1, arr2)
    OutputToFile(ID1, ID2, Distances)

def CalculateArrayDistances(arr1, arr2):
    global Coords1, Coords2, IDs1, IDs2, filename2
    # Find distances
    Distances = []
    ID1 = []
    ID2 = []
    i = 0
    while i < len(arr1):
        # Check that the coordinates are correct
        gps1 = arr1[i]
        gps2 = arr2[i]

        # Find the IDs
        if IDs1 != -1:
            ID1.append(gps1[IDs1])
        else:
            ID1.append("Line " + str(i+1))

        if IDs2 != -1 and filename2 != "":
            ID2.append(gps2[IDs2])
        elif filename2 != "":
            ID2.append("Line " + str(i+1))
        else:
            # We don't have a filename2
            ID2.append(gps2[IDs1])

        # Calculate the distances between the coordinates
        Lat1 = float(gps1[Coords1['lat']])
        Lat2 = float(gps2[Coords2['lat']])
        Lon1 = float(gps1[Coords1['lon']])
        Lon2 = float(gps2[Coords2['lon']])
        Distances.append(Haversine(Lat1,Lon1,Lat2,Lon2))
        i = i + 1
    return [ID1, ID2, Distances]

def OutputToFile(ID1, ID2, Distances):
    global outputfile
    # Output to file
    f = csv.writer(open(outputfile, "wb"), delimiter=Delimiter, quotechar=QuoteChar)
    i = 0
    while i < len(Distances):
        msg = []
        msg.append(str(ID1[i]))
        msg.append(str(ID2[i]))
        msg.append(str(Distances[i]))
        f.writerow(msg)
        i = i + 1

def Err(msg):
    print(msg)
    sys.exit()

# As seen on http://www.movable-type.co.uk/scripts/latlong.html
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
{% endhighlight %}