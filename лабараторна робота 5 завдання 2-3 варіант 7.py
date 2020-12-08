with open('Probne.txt') as file:
    words=0
    characters=0
    
    for line in file:
       
        listofinterrogativesentences=line.split()
        interrogative=interrogative+len(listofinterrogativesentences)
        characters += sum(len(word) for word in wordslist)

print(words)
print(characters)
