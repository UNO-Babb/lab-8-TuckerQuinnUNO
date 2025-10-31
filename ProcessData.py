#ProcessData.py
#Name: Tucker
#Date: Quinn
#Assignment: Process Data

import random

def main():

  #Open the files we will be using
  inFile = open("names.dat", 'r')
  outFile = open("StudentList.csv", 'w')
  inFile

  linecount = 0 
  for line in inFile:
    splitLine = line.split()
    entry = []
    firstName = splitLine[0]
    lastName = splitLine[1]
    studentid = splitLine[3]

    year = splitLine[5]
    major = splitLine[6]   # this neglects majors with multiple words but we only need to look at the first word
    abvmaj = major[:3]
    if year == "Freshman":
      abvyear = "Fr"
    elif year == "Sophomore":
      abvyear = "SO"
    elif year == "Junior":
      abvyear = "JR"
    elif year == "Senior":
      abvyear = "SR"
    last3 = studentid[8:]
    finitial = firstName[0]
    entry.append(lastName)
    entry.append(firstName)
    while len(lastName) < 5:
      lastName = lastName + "X"
    userID = finitial + lastName + last3
    majyear = abvmaj + "-" + abvyear
    entry.append(userID)
    entry.append(majyear)
    outFile.write("," .join(entry) + "\n")




    
 

  #Process each line of the input file and output to the CSV file

 

  #Close files in the end to save and ensure they are not damaged.
  inFile.close()
  outFile.close()

if __name__ == '__main__':
  main()
