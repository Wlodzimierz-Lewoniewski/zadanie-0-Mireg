import re

docs_number = int(input('Ilość dokumentów'))
documents = []

for _ in range(docs_number):
    doc_text = input()
    documents.append(doc_text)

queries_number = int(input('Liczba zapytań'))
queries = []

for _ in range(queries_number):
    query = input()
    queries.append(query)

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