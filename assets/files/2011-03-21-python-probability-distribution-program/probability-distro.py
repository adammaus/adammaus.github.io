import os, sys, random, math

#Open file of data
OutputFile = "Excel"

# Create the probability distro with the given number of bins
NumBins = 20
fileNames = ['temp.net']  # Remove file name to see different gaussian distributions
SuppressOutput = False     # True = show different diagnostic output

#############################

# Create a gaussian random number
def gauss(sigma):
    return sigma*math.sqrt(-2*math.log(random.random()))*math.sin(6.283185307*random.random())

data = {}
lengths = {}
i = 0
if len(fileNames) != 0:
    for x in fileNames:
        f = open(x, "r")
        data[i] = f.readlines()
        lengths[i] = float(len(data[i]))
        f.close()
        i = i + 1

else:
    while (i < 3):
        sigma = random.random()
        offset = random.random()*5
        arr = []
        j = 0
        while (j < 10000):
            arr.append(gauss(sigma)+offset)
            j = j + 1

        data[i] = arr
        lengths[i] = float(len(arr))
        i = i + 1

# Convert the data to floats
vect = []
tempData = {}
for y in data:
    temp = []
    for x in data[y]:
        vect.append(float(x))
        temp.append(float(x))

    tempData[y] = temp
data = tempData

# Find the max and min of the data
Top = max(vect)
Bot = min(vect)
NumBins = float(NumBins)

# Divide the range between top and bot into the num bins
Delta = (Top - Bot) / NumBins

if not SuppressOutput:
    print("Found ", len(data), " different time series")
    print("There are ", len(vect), " points total")
    print("Max of data: ", Top, "\nMin of data: ", Bot, "\n")
    print("Starting to Bin Data")

# Create a range vector
Range = []
Counts = []
i = Bot
while (i < Top):
    Range.append(i)
    count = {}
    for y in data:
        count[y] = 0

    Counts.append(count)
    i = i + Delta

# Put the data into the range
for y in data:
    for x in data[y]:
        # Find where this data point should be
        i = 0
        flag = True
        while (i < len(Range)-1 and flag):
            if (x >= Range[i] and x < Range[i+1]):
                flag = False
            else:
                i = i + 1

        Counts[i][y] = Counts[i][y] + 1

# Create Excel file by first creating an html file with a table
# then read the html file and convert it to excel (it is just easier to do)
if not SuppressOutput:
    print("Finised Binning the Data")
    print("Starting to create the Excel Sheet")

html = "<table>"
i = 0
while (i < len(Counts)):
    html += "<tr><td>" + str(Range[i]) + "</td>"
    for y in data:
        html += "<td>" + str(Counts[i][y] / lengths[y]) + "</td>"

    html += "</tr>"
    i = i + 1

html += "</table>"

f = open(OutputFile + ".html", "w") # Store data as temporary html file
f.write(html)
f.close()
f = open(OutputFile + ".html", "r")

f2 = open(OutputFile + ".xls", "w")
f2.write(str(f.readlines()[0]))
f2.close()

if not SuppressOutput:
    print("Completed Excel File")

f.close()

os.remove(OutputFile + ".html")     # Remove temporary file
