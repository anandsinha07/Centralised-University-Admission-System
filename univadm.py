from pandas.tools.plotting import parallel_coordinates
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv


ReadFile = open('univadm.csv', 'r')
Reader = csv.reader(ReadFile)

readi = list(Reader)
arrsum = list()

li = [6, 5, 8, 9, 6, 4, 3, 4, 4, 7]

for x in range (1, 16):
	sum = 0
	for y in range(1, 10):
		sum += float(readi[x][y]) * li[y-1]
	arrsum.append(sum)

print (arrsum)



ReadFile.close()


WriteFile = open('univadm.csv', 'w')
Writer = csv.writer(WriteFile)
readi[0][10] = "Total"

for x in range(1, 16):
	readi[x][9] = str(arrsum[x-1])

with WriteFile:
	Writer.writerows(readi)

WriteFile.close()





