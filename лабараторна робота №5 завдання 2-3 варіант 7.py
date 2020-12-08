with open('Probne.txt') as file:
    words=0
    characters=0
    
    for line in file:
        list of interrogative sentences =line.split()
        words=words+len(list of interrogative sentences)
        characters += sum(len(word) for word in wordslist)

print(words)
print(characters)
