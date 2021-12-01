import lightrdf
import re

owl_path = './CSO.owl'

data = []
doc = lightrdf.RDFDocument(owl_path)

for triple in doc.search_triples(None, None, None):
    line = []
    for v in triple:
        line.append(v)
    data.append(line)

word = input("Enter a word: ")

for n1, m, n2 in data:
    if 'superTopicOf' in m and (re.search(word + r"$", n1) or re.search(word + r"$", n2)):
        print(n1, m, n2)