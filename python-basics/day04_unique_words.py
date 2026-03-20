## Create day04_unique_words.py that 
## reads a sentence and prints unique words using a set.

sentence = input("Enter the sentence: ")
sentence = sentence.lower().split()
unique_words = set(sentence)

print(f"Unique words in the sentence: {unique_words}")