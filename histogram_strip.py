# Modules
import sys
import string
from collections import Counter


# Read file and count words
def read_paragraph(filename):
    wordcounter = Counter()
    with open(filename, 'r') as f:
        for line in f:
            words_wo_punctuation = []
            for word in line.lower().split():
                print(word)
                words_wo_punctuation.append(word.strip(string.punctuation))
            wordcounter.update(words_wo_punctuation)
        write_file(wordcounter)


# Write the count for each word to a file
def write_file(wordcount):
    for word, count in wordcount.most_common():
        # Write to the file with formatting dependant on longest word
        print("{:>{width}} | {} ({})\n".format(word, '='*count, count, width=max(map(len, wordcount))))
    
# Main function
if __name__ == '__main__':
	try:
		read_paragraph(sys.argv[1])
	except IndexError:
		print('>>> ERROR: Must specify file to read.')
		sys.exit(1)
