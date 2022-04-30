#!/usr/bin/env python3
import pickle
import random 
import numpy as np

file = ["sylListEnglish.pkl", "sylListFinnish.pkl"]

def getSample(fname):
	newSample = []
	a_file = open(fname, "rb")
	sylList = pickle.load(a_file)
	for i in range(500):
		newSample.append(random.choice(sylList))
	return newSample

for i in range(2):
	print(getSample(file[i]))
	
finnishDistSample = np.random.geometric(p=0.476, size=500)
englishDistSample = np.random.geometric(p=0.722, size=500)

print(finnishDistSample)
print(englishDistSample)