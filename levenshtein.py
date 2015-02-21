#! /usr/bin/python

def _delete(string, position):
	print "delete", string, "position", position 
	return string[:position] + string[position + 1:]
def _insert(string, letter, position):
	print "_insert", string, "position", position, "letter", letter 
	return string[:position] + letter + string[position:]	
def _substitute(string, letter, position):
	print "_substitute", string, "position", position, "letter", letter 
	return string[:position] + letter + string[position+1:]
	
def levenshtein_distance(string1, string2):
	graph = {}
	for position, letter in enumerate(string1):
		options = [_delete(string1, position), _insert(string1,string2[position], position), _substitute(string1,string2[position], position)]
		print options
		graph[letter] = options
	return graph

if __name__ == '__main__':
	import sys
	word1, word2 = (sys.argv[1], sys.argv[2])
	print _delete(word1, 0)
	graph = levenshtein_distance(word1, word2)
	print graph