string1 = "I do not like green eggs and ham."
list1 = [2, 5, 12, 6, 1, -5, 8, 5, 6, -2, 2, 27]
list2 = [-5, 6, 4, 8, 15, 16, 23, 42, 2, 7]
words = ["I", "do", "not", "like", "green", "eggs", "and", "ham", "I", "do", "not", "like", "them", "Sam", "I", "am"]

"""
Write a function that takes a string and produces a dictionary with
all distinct elements as the keys, and the number of each element as
the value
Bonus: do the same for a file (i.e. twain.txt)
"""
def count_unique(string1):
	#take string and make into list of words called my_list
    my_list = string1.split()
    #initialize dictionary
    d = {}
    # iterate through words in list
    for word in my_list:
    	#for each word, see if word is in d, if it is add 1 to its value
    	#if not, key = word and value = 0 (default value), then add 1 to value
    	d[word] = d.get(word, 0) + 1

    return d 

print count_unique(string1) 




"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
	#create set of unique unordered items(no duplicates) from list2 and use intersection to find values in common with list1
	#create list of common values and call it in_common
  	in_common = list(set(list2).intersection(list1))

	return in_common

print common_items(list1, list2)
    
    



"""
Given two lists, (without using 'if __ in ____' or 'index')
return a list of all common items shared between both lists. This time,
use a dictionary as part of your solution.
"""
def common_items2(list1, list2):
    d = {}
    # looks for item from list1 in dictionary and if it finds it does nothing, else it sets value to 1, all of our keys in d have value 1 at this point
    for item in list1:
    	d[item] = d.get(item, 1)
    # looks to see if item in list2 is in d, and if it finds it adds 1 to its value, now we have some keys with a value > 1
    #if it is not already in d it adds key to d and sets its value to default 0 + 1
    for item in list2:

    	d[item] = d.setdefault(item, 0) + 1
    #initializes empty list for our items in common
    in_common = []
    # iterates through d
    #if the value for a key is equal to 2, we know that it is a duplicate, so we append it to in_common 
    for key,value in d.iteritems():
    	if value == 2:
    		in_common.append(key)

    return in_common

print common_items2(list1, list2)

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
	#initialize dictionary
    d = {}
    #initialize list of negative values
    negs = []
    # iterate throuh list1
    #if 
    for num in list1:
    	#create temp var equal to number * -1
    	neg_num = num * -1
    	#append negative value to negs list
    	negs.append(neg_num)
    #Take list of negative numbers and list1, zip together and create a dictionary with dict(), works if both lists are the same length
    d = dict(zip(list1, negs))
    
    return d 

print sum_zero(list1)




"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):

	duplicates = {}
	#for each word in list words, uses get method to search for the word in duplicates
	#if it finds the word it does not change the dictionary
	#if it is not in the dictionary already, it adds the key and sets its value to 0
	#keys() returns list of keys which are our words without the duplicates 
	for word in words:
		duplicates[word] = duplicates.get(word, 0)


	return duplicates.keys()

print find_duplicates(words)




"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    d = {}

    for word in words:
    	d[len(word)] = d.setdefault(len(word), [])
    	d[len(word)].append(word)
    	
    pairs = sorted(d.items())
    for pair in pairs:
    	for word in pair[1]:
    		print word
    

print word_length(words)

"""
Here's a table of English to Pirate translations
English     Pirate

sir         matey
hotel       fleabag inn
student     swabbie
boy         matey
madam       proud beauty
professor   foul blaggart
restaurant  galley
your        yer
excuse      arr
students    swabbies
are         be
lawyer      foul blaggart
the         th'
restroom    head
my          me
hello       avast
is          be
man         matey

Write a program that asks the user to type in a sentence and then
print the sentece translated to pirate.
"""
