import spacy
nlp = spacy.load('en_core_web_md')

word1 = nlp("cat")
word2 = nlp('monkey')
word3 = nlp('banana')

# use similarity method to compare similarity levels between each word
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# it makes sense that NLP has deduced that the strongest relationship is between cat and monkey as they are both animals 
# NLP has also figured out that monkeys eat bananas therefore these two words have the second strongest similarity
# According to the internet Cats are actually a big fan of bananas, but I suppose this isn't common knowledge for NLP and therefore has the weakest similarity of 0.22
print()
word1 = nlp("bed")
word2 = nlp('sofa')
word3 = nlp('hammock')

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# I find the result for this interesting because you could argue that a bed is more similar to a hammock as the intended use for both is sleeping, whereas sofa's are more for sitting
# I suppose NLP has matched up bed and sofa as the strongest similarity because the words sofa and bed are often used together for a pull out sofa bed
# hammock and bed has the weakest similarity according to NLP, hammocks are very different to beds because theyre found in outdoor settings and are usually just a cotton sheet,
# but beds and sofas are both similar structures that use similar materials
print()

# This code will compare the similarity level between a series of words, for example, first it will calculate the similarity between
# cat and cat, cat and apple, cat and monkey and cat and banana, we use a nested loop for this
tokens = nlp('cat apple monkey banana')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))


# this code compares a sentence with numerous other sentences
sentence_to_compare = 'Why is my cat on the car'

sentences = ["where did my dog go",
'Hello, there is my car',
'I\'ve lost my car in my car',
'I\'d like my boat back',
'I will name my dog Diana']

model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


