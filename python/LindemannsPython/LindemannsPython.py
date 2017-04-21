import nltk
import numpy

texts = ["I love Python 123.",
         "R is good for analytics!",
         "Mathematics is funny."]

# import all necessary libraries
from nltk.stem import PorterStemmer
from nltk.tokenize import SpaceTokenizer
from nltk.corpus import stopwords
from functools import partial
#from gensim import corpora
#from gensim.models import TfidfModel
import re

# initialize the instances for various NLP tools
tokenizer = SpaceTokenizer()
stemmer = PorterStemmer()
 
# define steps
pipeline = [lambda s: re.sub('[\n]', '', s),
            lambda s: re.sub('[^\w\s]', '', s),
            lambda s: re.sub('[\d\n]', '', s),
            lambda s: s.lower(),
            lambda s: ' '.join(filter(lambda s: not (s in stopwords.words('english')), tokenizer.tokenize(s))),
            lambda s: ' '.join(map(lambda t: stemmer.stem(t), tokenizer.tokenize(s)))
           ]
 
# function that carries out the pipeline step-by-step
def preprocess_text(text, pipeline):
    if len(pipeline)==0:
        return text
    else:
        return preprocess_text(pipeline[0](text), pipeline[1:])
 
# preprocessing
preprocessed_texts = map(partial(preprocess_text, pipeline=pipeline), texts)

texts = ["I\n love Python\n 123.",
         "R is good for analytics!",
         "Mathematics is funny."]

# preprocessing
preprocessed_texts = map(partial(preprocess_text, pipeline=pipeline), texts)

#a = stopwords.words('english')

#This section reads in documents from the selected corpus as real text

#texts2 = ["FRENCH FREE MARKET CEREAL EXPORT BIDS DETAILED\n  French operators have requested licences\n  to export 320,000 tonnes of free market barley, 225,000 tonnes\n  of maize, 25,000 tonnes of free market bread-making wheat and\n  20,000 tonnes of feed wheat at today's EC tender, trade sources\n  said.\n      For the barley, rebates of between 138 and 141.25 European\n  currency units (Ecus) per tonne were sought, for maize they\n  were between 129.65 and 139 Ecus, for bread-making wheat around\n  145 Ecus and for feed wheat around 142.45 Ecus.\n      Barley rebates of up to 138.50 Ecus were requested for a\n  total of 40,000 tonnes and at 139 Ecus for 85,000 tonnes.\n      Rebates of up to 130 Ecus per tonne were requested for a\n  total of 55,000 tonnes maize and up to 131 Ecus for 105,000\n  tonnes, the sources said.\n  \n\n"]

#preprocessed_texts2 = map(partial(preprocess_text, pipeline=pipeline), texts2)

from nltk.corpus import reuters 

ActiveIds = reuters.fileids('barley')

unsortedWords = set()

for id in ActiveIds:
    RawText = [reuters.raw(id)]
    procText = list(map(partial(preprocess_text, pipeline=pipeline), RawText))
    words = set(procText[0].split())
    unsortedWords.update(words)

sortedWords = sorted(unsortedWords)
numberOfDocuments = len(ActiveIds)
numberOfWords = len(sortedWords)

wordCountMatrix = numpy.zeros([numberOfWords,numberOfDocuments])

docCounter = 0;
for id in ActiveIds: 
    RawText = [reuters.raw(id)]
    fileStr = "textDocument_" + str(docCounter) + ".txt"
    filePtr3 = open(fileStr, "w")
    filePtr3.write("{}".format(RawText[0]))
    filePtr3.close()
    procText = list(map(partial(preprocess_text, pipeline=pipeline), RawText))
    words = set(procText[0].split())
    for wd in words:
        foundWord = sortedWords.index(wd)
        wordCountMatrix[foundWord][docCounter] += 1
    docCounter += 1
    #print(docCounter)

pairedWordsMatrix = numpy.matmul(wordCountMatrix,wordCountMatrix.transpose())

lowerPairedWordsBound = 5
upperPairedWordsBound = 7

filePtr = open(r"test3LevelFile.txt", "w")
filePtr2 = open(r"testWordListFile.txt", "w")

prevRow = -1

for row in range(numberOfWords):
    filePtr2.write("{}\n".format(sortedWords[row]))
    if pairedWordsMatrix[row,row] >= lowerPairedWordsBound:
        for column in range(numberOfWords):
            if pairedWordsMatrix[column,column] >= lowerPairedWordsBound:
                value = pairedWordsMatrix[row,column]
        #for (row, column), value in numpy.ndenumerate(pairedWordsMatrix):
                #print(row, column, value)
                if pairedWordsMatrix[row,column] >= lowerPairedWordsBound and \
                    pairedWordsMatrix[row,column] <= upperPairedWordsBound and \
                    row != column:
                    if row != prevRow:
                        if prevRow > -1:
                            filePtr.write("\n")
                        prevRow = row
                        filePtr.write("{} ".format(row))
                    filePtr.write("; {} ".format(column))
                    docCounter = -1
                    for id in ActiveIds:
                        docCounter += 1
                        if wordCountMatrix[row][docCounter] > 0 and wordCountMatrix[column][docCounter] > 0:
                            filePtr.write(", {} ".format(docCounter))

filePtr.close()
filePtr2.close()


#This section creates separate document files for display.

#This section performs standard text preprocessing functions
#The result is lists of words.

#Create list of words, list of documents, and associated three 
#level list for display purposes.