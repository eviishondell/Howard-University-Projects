def inchesToFeet(inches):
	return inches / 12

def feetToInches(feet):
	return feet * 12


def feetToYards(feet):
    return feet / 3

def yardsToFeet(yards):
    return yards * 3


def yardsToMiles(yards):
    return yards / 1760
    
def milesToYards(miles):
    return miles * 1760
    

#def yardsToFeet(yards)
    #return yards / 

#milesToYards(miles)

def feetToNauticalMiles(feet):
    return feet / 6080
    
def nauticalMilesToFeet(nauticalMiles):
    return nauticalMiles * 6080
#############################################################

def inchesToMiles(inches):
    return yardsToMiles(feetToYards(inchesToFeet(inches)))

def milesToInches(miles):
    return feetToInches(yardsToFeet(milesToYards(miles)))
    
    
    
    
def milesToNauticalMiles(miles):
    return feetToNauticalMiles(yardsToFeet(milesToYards(miles)))
    
def nauticalMilesToMiles(NauticalMiles):
    return yardsToMiles(feetToYards(nauticalMilesToFeet(NauticalMiles)))



def printFeetAndInches(value):
    inInches = feetToInches(value)
    inFeet = inchesToFeet(value)
    print(str(value) + " feet is " + str(round(inInches, 5)) + " inches.")
    print(str(value) + " inches is " + str(round(inFeet, 5)) + " feet.")

def printMilesAndNauticalMiles(value):
    inNauticalMiles = milesToNauticalMiles(value)
    inMiles = nauticalMilesToMiles(value)
    print(str(value) + " miles is " + str(round(inNauticalMiles, 5)) + " nautical miles.")
    print(str(value) + " nautical miles is " + str(round(inMiles, 5)) + " miles.")
    
    

def TwipsToPoints(twips):
	return twips / 20

def PointsToTwips(points):
    return points * 20
    
def PointsToLine(points):
    return points / 6
    
def lineToPoints(lines):
    return lines * 6
    
def lineToPoppyseeds(line):
    return line / 1
    
def lineToInches(line):
    return line / 12
    
def PoppyseedsToLine(Poppyseeds):
    return Poppyseeds * 1
    


#def inchesToMiles(inches):
    #return yardsToMiles(feetToYards(inchesToFeet(inches)))

#def milesToInches(miles):
    #return feetToInches(yardsToFeet(milesToYards(miles)))
#############################################################
def twipsToPoppyseeds(Twips):
    return lineToPoppyseeds(PointsToLine(TwipsToPoints(Twips)))
    
def PoppyseedsToTwips(Poppyseeds):
    return PointsToTwips(lineToPoints(PoppyseedsToLine(Poppyseeds)))
    
    

def printTwipsAndPoppyseed(value):
    inPoppyseeds = twipsToPoppyseeds(value)
    inTwips = PoppyseedsToTwips(value)
    print(str(value) + " poppyseeds is " + str(round(inTwips, 5)) + " twips.")
    print(str(value) + " twips is " + str(round(inPoppyseeds, 5)) + " poppyseeds.")
    
# Write all of your code above this line.
# This is to make the tests run.
import sys
if len(sys.argv) > 1 and sys.argv[1] == 'feet':
	printFeetAndInches(10)

if len(sys.argv) > 1 and sys.argv[1] == 'ratio':
	printMilesAndNauticalMiles(10)

if len(sys.argv) > 1 and sys.argv[1] == 'twips':
	printTwipsAndPoppyseed(10)
