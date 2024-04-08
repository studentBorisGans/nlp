# https://www.geeksforgeeks.org/python-text-summarizer/
# importing libraries 
import nltk 
# nltk.download()
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize, sent_tokenize 

# Input text - to summarize 
text = "The entity I’ve chosen to research about in Africa is the Kushite Kingdom, which was the most powerful Nubian state of the early 2nd millennium BCE. The Kingdom of Kush was founded in 1700 BCE in the south of Egypt, and reached its peak during the Second Intermediate Period in Egypt when they formed an alliance with the Hyksos (the kings of the 15th Dynasty of Egypt) between 1650-1550 BCE. It was during this period that the capital of the Kushite Kingdom, Kerma, flourished. Although only about 2,000 people lived in the city of Kerma, Kerma culture stretched for about 200 miles beyond the city. After coming into conflict with the Hyksos, however, they were overtaken by the Egyptians around 1500 BCE. It wasn’t until the New Kingdom collapsed in 1050 BCE that the Kushite people could come back to power. By 727 BCE the Kushite King Piankhi conquered Egypt which was divided by rival dynasties, presenting himself as pharaohs who could return Egypt to its former glory. Piankhi founded the 25th Dynasty of Egypt, also known as the “Black Pharaohs”, and the Kushite state had a territory that stretched from the Mediterranean until the Fifth Cataract until the year 657 BCE in which the Neo-Assyrian empire conquered Egypt. The Kushites fled to Meroe, a city/area in Sudan, which continued to flourish for many years following, and the last Kushite king’s rule ended in about 300 BCE."
# Tokenizing the text 
stopWords = set(stopwords.words("english")) 
words = word_tokenize(text) 

# Creating a frequency table to keep the 
# score of each word 

freqTable = dict() 
for word in words: 
	word = word.lower() 
	if word in stopWords: 
		continue
	if word in freqTable: 
		freqTable[word] += 1
	else: 
		freqTable[word] = 1

# Creating a dictionary to keep the score 
# of each sentence 
sentences = sent_tokenize(text) 
sentenceValue = dict() 

for sentence in sentences: 
	for word, freq in freqTable.items(): 
		if word in sentence.lower(): 
			if sentence in sentenceValue: 
				sentenceValue[sentence] += freq 
			else: 
				sentenceValue[sentence] = freq 



sumValues = 0
for sentence in sentenceValue: 
	sumValues += sentenceValue[sentence] 

# Average value of a sentence from the original text 

average = int(sumValues / len(sentenceValue)) 

# Storing sentences into our summary. 
summary = '' 
for sentence in sentences: 
	if (sentence in sentenceValue) and (sentenceValue[sentence] > (1.2 * average)): 
		summary += " " + sentence 
print(summary) 
