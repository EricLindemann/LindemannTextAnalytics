import nltk
import numpy

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

fileStr = "textDocuments.txt"
filePtr3 = open(fileStr, "w")

docCounter = 0;
for id in ActiveIds: 
    RawText = [reuters.raw(id)]
    filePtr3.write("ZZZ{}ZZZ\n".format(RawText[0]))
    procText = list(map(partial(preprocess_text, pipeline=pipeline), RawText))
    words = set(procText[0].split())
    for wd in words:
        foundWord = sortedWords.index(wd)
        wordCountMatrix[foundWord][docCounter] += 1
    docCounter += 1
    #print(docCounter)

filePtr3.close()

pairedWordsMatrix = numpy.matmul(wordCountMatrix,wordCountMatrix.transpose())

lowerPairedWordsBound = 5
upperPairedWordsBound = 7

for row in range(numberOfWords-1, -1, -1):
    if pairedWordsMatrix[row,row] < lowerPairedWordsBound:
        numpy.delete(pairedWordsMatrix, row, axis=0)
        numpy.delete(pairedWordsMatrix, row, axis=1)
        numpy.delete(wordCountMatrix, row, axis=0)
        sortedWords.pop(row)

newNumberOfWords = len(sortedWords)

filePtr2 = open(r"wordListFile.txt", "w")

for row in range(newNumberOfWords):
    filePtr2.write("{}\n".format(sortedWords[row]))

filePtr2.close()

filePtr = open(r"test3LevelFile.txt", "w")

prevRow = -1

for row in range(newNumberOfWords):
    if pairedWordsMatrix[row,row] >= lowerPairedWordsBound:
        for column in range(newNumberOfWords):
            if pairedWordsMatrix[column,column] >= lowerPairedWordsBound:
                value = pairedWordsMatrix[row,column]
                print(row, column, value)
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


