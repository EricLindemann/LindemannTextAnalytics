import nltk
import numpy
import os

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
 
#This section reads in documents from the selected corpus as real text

from nltk.corpus import reuters 

#This reads in all documents and finds all unique words

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

#This creates a matrix that counts all cross-occurrences of each pair of words in all documents:

wordCountMatrix = numpy.zeros([numberOfWords,numberOfDocuments])

docCounter = 0;
for id in ActiveIds: 
    RawText = [reuters.raw(id)]

    procText = list(map(partial(preprocess_text, pipeline=pipeline), RawText))
    words = set(procText[0].split())
    for wd in words:
        foundWord = sortedWords.index(wd)
        wordCountMatrix[foundWord][docCounter] += 1
    docCounter += 1
    #print(docCounter)

pairedWordsMatrix = numpy.matmul(wordCountMatrix,wordCountMatrix.transpose())

#This reduces the various data structures to only include active combinations:

lowerPairedWordsBound = 7
upperPairedWordsBound = 7

goodRows = numpy.zeros(numberOfWords)
goodColumns = numpy.zeros(numberOfWords)
goodDocs = numpy.zeros(numberOfDocuments)

for row in range(numberOfWords):
    if pairedWordsMatrix[row,row] >= lowerPairedWordsBound:
        for column in range(numberOfWords):
            if pairedWordsMatrix[column,column] >= lowerPairedWordsBound:
                if pairedWordsMatrix[row,column] >= lowerPairedWordsBound and \
                    pairedWordsMatrix[row,column] <= upperPairedWordsBound and \
                    row != column:
                    goodRows[row] = 1
                    goodColumns[column] = 1

                    docCounter = -1
                    for id in ActiveIds:
                        docCounter += 1
                        if wordCountMatrix[row][docCounter] > 0 and wordCountMatrix[column][docCounter] > 0:
                            goodDocs[docCounter] = 1
    
newNumberOfWords = numpy.sum(goodRows).astype("int")
newNumberOfDocuments = numpy.sum(goodDocs).astype("int")
newSortedWords = []
newWordCountMatrix = numpy.zeros([newNumberOfWords,newNumberOfDocuments])

newRow = -1
for row in range(numberOfWords):
    if goodRows[row] == 1:
        newRow += 1
        newSortedWords.append(sortedWords[row])
        docCounter = -1
        newDocCounter = -1
        for id in ActiveIds:
            docCounter += 1
            if goodDocs[docCounter] == 1:
                newDocCounter += 1
                newWordCountMatrix[newRow][newDocCounter] = wordCountMatrix[row][docCounter]

del wordCountMatrix
del pairedWordsMatrix

newPairedWordsMatrix = numpy.matmul(newWordCountMatrix,newWordCountMatrix.transpose())

#for revRow in range(numberOfWords):
#    row = numberOfWords - revRow - 1
#    if goodRows[row] == 0 and goodColumns[row] == 0:
#        numpy.delete(pairedWordsMatrix, row, axis=0)
#        numpy.delete(pairedWordsMatrix, row, axis=1)
#        numpy.delete(wordCountMatrix, row, axis=0)
#        numpy.delete(goodRows, row, axis=0)
#        numpy.delete(goodColumns, row, axis=0)

#        sortedWords.pop(row)

pathToData = os.path.join(os.path.dirname(__file__), os.path.realpath('..\\..\\..\\data'))

wordListFile = os.path.join(pathToData, "wordListFile.txt")

filePtr2 = open(wordListFile, "w")

for row in range(newNumberOfWords):
    filePtr2.write("{}\n".format(newSortedWords[row]))

filePtr2.close()

#This reruns the entire analysis, but only with "good" words

threeLevelFile = os.path.join(pathToData, "threeLevelFile.txt")

filePtr = open(threeLevelFile, "w")

prevRow = -1

for row in range(newNumberOfWords):
    for column in range(newNumberOfWords):
        if newPairedWordsMatrix[row,column] >= lowerPairedWordsBound and \
            newPairedWordsMatrix[row,column] <= upperPairedWordsBound and \
            row != column:
            if row != prevRow:
                if prevRow > -1:
                    filePtr.write("\n")
                prevRow = row
                filePtr.write("{} ".format(row))
            filePtr.write("; {} ".format(column))
            for newDocCounter in range(newNumberOfDocuments):
                if newWordCountMatrix[row][newDocCounter] > 0 and newWordCountMatrix[column][newDocCounter] > 0:
                    filePtr.write(", {} ".format(newDocCounter))

filePtr.close()

textDocumentsFile = os.path.join(pathToData, "textDocuments.txt")

filePtr3 = open(textDocumentsFile, "w")

textHeadersFile = os.path.join(pathToData, "textHeaders.txt")

filePtr4 = open(textHeadersFile, "w")

docCounter = -1;
for id in ActiveIds: 
    docCounter += 1
    if goodDocs[docCounter] == 1:
        RawText = [reuters.raw(id)]

        #This splits the documents into 2 files -- one with headers, the other with bodies:

        lhs, rhs = RawText[0].split("\n", 1)

        filePtr3.write(" \\**\\ {} \\**\\ \n".format(rhs))
        filePtr4.write(" \\**\\ {} \\**\\ \n".format(lhs))

filePtr3.close()
filePtr4.close()

