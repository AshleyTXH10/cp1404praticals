"""
Word Occurrences
Estimate: 20 minutes
Actual: 15 minutes
"""
text = input("Text: ")
words = sorted(text.split())

word_count = {}
# Counts the amount of times a word appears
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

word_width = max(len(word) for word in word_count)

# Print word and the count in a formatted way
for word, count in word_count.items():
    print(f"{word:{word_width}} : {count}")
