import re

import nltk
from nltk import SnowballStemmer
import lightrdf

stemmer = SnowballStemmer(language='english')
inputFilename = './pos_computer_science.txt'
ontologyFilename = './CSO.owl'
outputFilename = './newOntologyWords.txt'

data = []
doc = lightrdf.RDFDocument(ontologyFilename)
for triple in doc.search_triples(None, None, None):
    line = []
    for v in triple:
        line.append(v)
    data.append(line)

illegalChars = ['(', ')', ',', '.', ' ', '?', '!', '[', ']']
with open(inputFilename, 'r', encoding="utf-8") as inputFile:
    with open(outputFilename, 'w', encoding="utf-8") as outputFile:
        for line in inputFile:
            for word in line.split(' '):
                if word in illegalChars:
                    continue
                exists = False
                # word = stemmer.stem(word)
                print(word)
                for n1, m, n2 in data:
                    if re.search(f"^{word}$", n1.split('/')[-1], flags=re.IGNORECASE):
                        outputFile.write(line)
                        exists = True
                        print(word, end='->')
                        print(n1)
                        break
                if exists:
                    break

