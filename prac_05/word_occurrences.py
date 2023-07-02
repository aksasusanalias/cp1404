
"""
Word Occurrences
Estimate: 20 minutes
Actual:   35 minutes
"""

text = input("Enter a string: ")
word_total = {}
words = text.split()
for word in words:
    if word in word_total:
        word_total[word] += 1
    else:
        word_total[word] = 1

max_word_length = max(len(word) for word in word_total)
for word, count in sorted(word_total.items()):
    print(f"{word:>{max_word_length}} : {count}")
