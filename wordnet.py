from nltk.corpus import wordnet

#get the synonyms
syns = wordnet.synsets("program")
print(syns[0].name())

#to get just the word
print(syns[0].lemmas()[0].name())

#to get the definition of the word
print(syns[0].definition())

#to get the examples of use of the word
print(syns[0].examples())

#synonyms and antonyms
synonyms = []
antonyms = []

for syn in wordnet.synsets("good"):
    for l in syn.lemmas():
        synonyms.append(l.name())
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())

print(set(synonyms))
print(set(antonyms))

#comparing the words(nouns)
w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('boat.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('car.n.01')
print(w1.wup_similarity(w2))

w1 = wordnet.synset('ship.n.01')
w2 = wordnet.synset('cat.n.01')
print(w1.wup_similarity(w2))