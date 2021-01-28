import csv, os

def writecsv(filename, the_list):
    with open(filename, 'w', newline = '') as f:
      a = csv.writer(f, delimiter = ',')
      a.writerows(the_list)



def opencsv(filename):
    f = open(filename, 'r')
    reader = csv.reader(f)
    output = []
        for i in reader:
          output.append(i)
        return output
