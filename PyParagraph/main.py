# Read text file and extract the following:
# Approximate word count
# Approximate sentence count
# Approximate letter count (per word)
# Average sentence length (in words)

import os
import csv

paragraph_data = os.path.join("../PyParagraph/raw_data", "paragraph_1.txt")
text_file = open(paragraph_data, "r")
paragraph = text_file.read()
# Get word count
word_count = paragraph.count(" ") +  1
space_count = paragraph.count(" ")
# Get sentence count
sentence_count = paragraph.count(".")
# find average letter count per word
# Get number of letters in string
stringLength = len(paragraph)
# omit periods and spaces
numberLetters = stringLength - sentence_count - space_count
avgLetterCount = numberLetters / word_count
# Find average sentence length
AvgSentenceLen = word_count / sentence_count 

# Output
print(f"Paragraph Analysis")
print(f"-----------------")
print(f"Approximate Word Count: {word_count}")
print(f"Approximate Sentence Count: {sentence_count}")
print(f"Average Letter Count: {avgLetterCount:.2}")
print(f"Average Sentence Length: {AvgSentenceLen}")
