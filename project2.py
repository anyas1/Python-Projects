# Make your own madlib

# Open story file
with open('story.txt', 'r') as f:
    story = f.read()

# Create a set of words
words = set()
start_of_word = -1

target_start = '<'
target_end = '>'

# Locates all words in story
for i, char in enumerate(story):
    if char == target_start:
        start_of_word = i

    if char == target_end and start_of_word != -1:
        word = story[start_of_word: i + 1]
        words.add(word)
        start_of_word = -1

# Generating answers
answers = {}

for word in words:
    answer = input('Enter a word for ' + word + ': ')
    answers[word] = answer

# Replacing instances of each word
for word in words:
    story = story.replace(word, answers[word])

# Prints story with updated strings
print(story)
