import re

import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
from nltk import SnowballStemmer

filename = './test'
newFilename = './pos_computer_science.txt'

stemmer = SnowballStemmer(language='english')


def valid_syntax(subjects, verbs):
    return (len(subjects) == 2 and len(verbs) == 1) and (subjects[0] < verbs[0] and subjects[1] > verbs[0])


with open(filename, 'r', encoding="utf-8") as inputText:
    with open(newFilename, 'w', encoding="utf-8") as outputText:
        for line in inputText:
            for phrase in re.split('\.!?', line):
                tokens = word_tokenize(phrase)

                for idx, string in enumerate(tokens):
                    tokens[idx] = stemmer.stem(string)
                tokens_pos = pos_tag(tokens)

                subjects = []
                verbs = []
                for idx, token in enumerate(tokens_pos):
                    if len(subjects) == 2 and len(verbs) == 1:
                        break

                    if re.search('^NN', token[1]):
                        print(f"SUBJ:{token} {phrase}")
                        subjects.append(idx)

                    if re.search('^VB', token[1]):
                        print(f"VERB:{token}")
                        verbs.append(idx)

                if not valid_syntax(subjects, verbs):
                    continue

                words = word_tokenize(phrase)
                # for index in subjects:
                #     words[index] = "!" + words[index] + "!"
                #
                # for index in verbs:
                #     words[index] = "<" + words[index] + ">"

                outputText.write(" ".join(words) + '\n')
