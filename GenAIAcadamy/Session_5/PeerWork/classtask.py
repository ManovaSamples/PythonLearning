#create function takes a list of word as input and returns longest word in the list

list = ["apple", "Yolanda", "banana", "Copenhagen"]
def longest_word(list):
    longest = ""
    for word in list:
      if len(word) > len(longest):
        longest = word
    return longest
print(longest_word(list))


def findLongestWord(words):
    longestWord = max(words, key=len)
    return longestWord

listOfWords = ["Name", "age", "work", "city"]
print(findLongestWord(listOfWords))

l=['hello','world','this','is','pyhtoncourse']
c=0
for i in l:
	if len(i)>c:
		greatest=i
		c=len(i)
print('the gretest string is',greatest)