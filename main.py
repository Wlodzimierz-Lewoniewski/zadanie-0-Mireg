import re

with open('input.txt', 'r') as file:
    data = file.read().splitlines()

docs_number = int(data[0])
documents = data[1:docs_number+1]

queries_number = int(data[docs_number+1])
queries = data[docs_number+2:]

counts = {}

for query in queries:
    pattern = re.compile(r"\b"+query+r"\b", re.IGNORECASE)
    for i,doc in enumerate(documents):
        matches = pattern.findall(doc)
        counts[i] = len(matches)
    #i - index of document, the program is suposed to return document number based on amount of time the query exist inside, in descending order.
        counts_filtered = {key: value for key, value in counts.items() if value != 0}
    
    docs_order = dict(sorted(counts_filtered.items(), key=lambda item: item[1], reverse=True))
    print(list(docs_order.keys()))