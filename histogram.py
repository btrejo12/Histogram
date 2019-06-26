# Modules
import sys
import string
from collections import Counter


# Read file and count words
def read_paragraph(filename):
	wordcounter = Counter()
	with open(filename, 'r') as f:
		for line in f:
			# Creates translator to remove punctuation
			translator = str.maketrans("", "", string.punctuation)
			line_wo_punctuation = line.translate(translator)
			words = line_wo_punctuation.lower().split()
			
			# Count words
			wordcounter.update(words)
		
		write_file(wordcounter)


# Write the count for each word to a file
def write_file(wordcount):
	with open('output.txt', 'w+') as w:
		for word, count in wordcount.most_common():
			# Write to the file with formatting dependant on longest word
			w.write("{:>{width}} | {} ({})\n".format(word, '='*count, count, width=max(map(len, wordcount))))
		
# Main function
if __name__ == '__main__':
	try:
		read_paragraph(sys.argv[1])
	except IndexError:
		print('>>> ERROR: Must specify file to read.')
		sys.exit(1)
