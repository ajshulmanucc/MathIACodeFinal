import nltk
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
import re
import string
from collections import Counter
import pickle
import syllables
numberOfTexts = 32
s = '<@ """@$ FSDF >something something <more noise>'
texts = ['OnLibertyF.txt', 'AroundTheWorldInEightyDaysE.txt', 'AnneofGreenGablesF.txt', 'GrimmsFairyTalesF.txt', 'OnLibertyE.txt', 'AroundTheWorldInEightyDaysF.txt', 'AnneofGreenGablesE.txt', 'GrimmsFairyTalesE.txt', 'AlicesAdventuresinWonderlandE.txt', 'PrideandPrejudiceF.txt', 'TheNarrativeofArthurGordonPymE.txt', 'ALittlePrincessF.txt', 'TheAdventuresofTomSawyerF.txt', 'AlicesAdventuresinWonderlandF.txt', 'PrideandPrejudiceE.txt', 'TheNarrativeofArthurGordonPymF.txt', 'ALittlePrincessE.txt', 'TheAdventuresofTomSawyerE.txt', 'ATaleofTwoCities(Book1)F.txt', 'TwoLittleSavagesE.txt', 'TreasureIslandE.txt', 'HamletE.txt', 'WhiteFangF.txt', 'ATaleofTwoCities(Book1)E.txt', 'TwoLittleSavagesF.txt', 'TreasureIslandF.txt', 'HamletF.txt', 'WhiteFangE.txt', 'ThePoeticsE.txt', 'ThePrinceE.txt', 'AllanandtheHolyFlowerF.txt', 'PhaedoE.txt', 'ThePoeticsF.txt', 'ThePrinceF.txt', 'AllanandtheHolyFlowerE.txt', 'PhaedoF.txt', 'TheCharingCrossMysteryF.txt', 'TheSilverHordeE.txt', 'RepresentativeMenE.txt', 'TessofthedUrbervillesF.txt', 'TheCharingCrossMysteryE.txt', 'TheSilverHordeF.txt', 'RepresentativeMenF.txt', 'TessofthedUrbervillesE.txt', 'TheBushBoysF.txt', 'AnOld-fashionedGirlF.txt', 'TheBushBoysE.txt', 'AnOld-fashionedGirlE.txt', 'TheBathComedyE.txt', 'TheProdigalSonF.txt', 'TheSonOfTarzanE.txt', 'TheJungleBookE.txt', 'TheBathComedyF.txt', 'TheProdigalSonE.txt', 'TheSonOfTarzanF.txt', 'TheJungleBookF.txt', 'ThePictureofDorianGrayE.txt', 'TheHoundoftheBaskervillesF.txt', 'TheAdventuresofPinocchioE.txt', 'ThePictureofDorianGrayF.txt', 'TheHoundoftheBaskervillesE.txt', 'TheAdventuresofPinocchioF.txt']

def getFreq(fname):
	sentences = [re.sub('<.*?>', '', x.replace('\n', '').replace('\r', '').replace('-', '')) for x in open("txtFiles/"+fname+".txt") if x]
	corpus = []
	allPunc = string.punctuation+"—“”“’````'''“’”'/|//"
	for s in sentences:
		for w in nltk.word_tokenize(s):
			if w not in allPunc: 
				corpus.append(syllables.estimate(''.join([i for i in w if not i.isdigit()])))
	a_file = open("pkl/"+fname+".pkl", "wb")
	pickle.dump(corpus, a_file)
	a_file.close()
	print(fname)

for i in texts:
	getFreq(i.replace('.txt', ''))
	
	
	