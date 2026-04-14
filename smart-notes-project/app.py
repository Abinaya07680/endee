# Smart Notes Search (Mini AI Project)

notes = [
    "Machine learning is about training models on data",
    "Neural networks are inspired by the human brain",
    "Databases store structured information",
    "Python is commonly used for AI development"
]

def similarity(a, b):
    wordsA = a.lower().split()
    wordsB = b.lower().split()
    
    count = 0
    for w1 in wordsA:
        for w2 in wordsB:
            if w1 == w2:
                count += 1
    return count

def search(query):
    best_match = ""
    max_score = -1

    for note in notes:
        score = similarity(query, note)
        if score > max_score:
            max_score = score
            best_match = note

    return best_match

print("🧠 Smart Notes Search")

while True:
    query = input("\nAsk something (type 'exit' to quit): ")

    if query.lower() == "exit":
        print("Goodbye 👋")
        break

    result = search(query)
    print("Answer:", result)
