#!/usr/bin/env python3
import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import re
import string
from collections import Counter
import pickle

import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats
import math


s = '<@ """@$ FSDF >something something <more noise>'
nameList = ['ATaleofTwoCities(Book1)E.pkl', 'TwoLittleSavagesF.pkl', 'WhiteFangE.pkl', 'TreasureIslandF.pkl', 'HamletF.pkl', 'ATaleofTwoCities(Book1)F.pkl', 'TwoLittleSavagesE.pkl', 'WhiteFangF.pkl', 'TreasureIslandE.pkl', 'HamletE.pkl', 'ThePoeticsF.pkl', 'AllanandtheHolyFlowerE.pkl', 'PhaedoF.pkl', 'ThePrinceF.pkl', 'ThePoeticsE.pkl', 'AllanandtheHolyFlowerF.pkl', 'PhaedoE.pkl', 'ThePrinceE.pkl', 'OnLibertyE.pkl', 'AroundTheWorldInEightyDaysF.pkl', 'GrimmsFairyTalesE.pkl', 'AnneofGreenGablesE.pkl', 'OnLibertyF.pkl', 'AroundTheWorldInEightyDaysE.pkl', 'GrimmsFairyTalesF.pkl', 'AnneofGreenGablesF.pkl', 'PrideandPrejudiceE.pkl', 'TheNarrativeofArthurGordonPymF.pkl', 'AlicesAdventuresinWonderlandF.pkl', 'TheAdventuresofTomSawyerE.pkl', 'ALittlePrincessE.pkl', 'PrideandPrejudiceF.pkl', 'TheNarrativeofArthurGordonPymE.pkl', 'AlicesAdventuresinWonderlandE.pkl', 'TheAdventuresofTomSawyerF.pkl', 'ALittlePrincessF.pkl', 'TheSonOfTarzanF.pkl', 'TheJungleBookF.pkl', 'TheBathComedyF.pkl', 'TheProdigalSonE.pkl', 'TheSonOfTarzanE.pkl', 'TheJungleBookE.pkl', 'TheBathComedyE.pkl', 'TheProdigalSonF.pkl', 'ThePictureofDorianGrayF.pkl', 'TheHoundoftheBaskervillesE.pkl', 'TheAdventuresofPinocchioF.pkl', 'ThePictureofDorianGrayE.pkl', 'TheHoundoftheBaskervillesF.pkl', 'TheAdventuresofPinocchioE.pkl', 'TheSilverHordeF.pkl', 'TheCharingCrossMysteryE.pkl', 'TessofthedUrbervillesE.pkl', 'RepresentativeMenF.pkl', 'TheSilverHordeE.pkl', 'TheCharingCrossMysteryF.pkl', 'TessofthedUrbervillesF.pkl', 'RepresentativeMenE.pkl', 'TheBushBoysE.pkl', 'AnOld-fashionedGirlE.pkl', 'TheBushBoysF.pkl', 'AnOld-fashionedGirlF.pkl']
sumOfFreq = [0]
def getFreq(fname):
	wordFreqOrder = []
	a_file = open("syllablesFile/"+fname, "rb")
	corpusRanked = pickle.load(a_file)
	for k,v in corpusRanked.items():
		wordFreqOrder.append(v)
	return(wordFreqOrder[:8])

fig, ax = plt.subplots(2, 1)

fig.suptitle("Word Length-Frequency of Different Texts (English vs. Finnish)")
fig.tight_layout()

ax1 = plt.subplot(2, 1, 1)
ax1.grid()
ax1.title.set_text('English Texts')
ax1.set_xlim(left=1, right=9)
ax1.set_ylim(bottom=0, top=0.8)

ax2 = plt.subplot(2, 1, 2, sharey=ax1, sharex=ax1)
ax2.title.set_text('Finnish Texts')
ax2.grid()


for i in nameList:
	name = i[:-5]
	if i[-5] == "E":
		sumOfFreqE = np.add(sumOfFreq, getFreq(i))
	elif i[-5] == "F":
		sumOfFreqF = np.add(sumOfFreq, getFreq(i))
		
	else:
		print("Final letter of "+i+"is not E or F")
x = [1,2,3,4,5,6,7,8]
ax1.scatter(x, sumOfFreqE, label = name)
ax2.scatter(x, sumOfFreqF, label = name)
ax1.plot(x, sumOfFreqE, label = name)
ax2.plot(x, sumOfFreqF, label = name)
ax1.set_ylabel('Relative Frequency')
ax1.set_xlabel('Syllable Count')
ax2.set_ylabel('Relative Frequency')
ax2.set_xlabel('Syllable Count')


plt.show()