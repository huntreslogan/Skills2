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
    my_list = string1.split()
    d = {}
    count = 1
    for item in my_list:
    	if item not in d:
	    	d[item] = count
    	else:
    		d[item] += 1

    return d 

print count_unique(string1) 




"""
Given two lists, (without using the keywords 'if __ in ____' or the method 'index')
return a list of all common items shared between both lists
"""
def common_items(list1, list2):
	
	


  	
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
    # looks for item from list1 in dictionary and if it finds it does nothing, else it sets value to 1
    for item in list1:
    	d[item] = d.get(item, 1)
    # looks for an item from list2 in d and if it finds it adds 1 to its value, if it is not in d it adds to d and sets value to default 0 + 1
    for item in list2:
    	d[item] = d.setdefault(item, 0) + 1

    in_common = []

    for key,value in d.iteritems():
    	if value >= 2:
    		in_common.append(key)

    return in_common

print common_items2(list1, list2)

"""
Given a list of numbers, return list of number pairs that sum to zero
"""
def sum_zero(list1):
    d = {}
    negs = []
    for e in list1:
    	neg_num = e * -1
    	negs.append(neg_num)
    d = dict(zip(list1, negs))
    return d 

print sum_zero(list1)




"""
Given a list of words, return a list of words with duplicates removed
"""
def find_duplicates(words):
    non_dupes = []
    
    for word in words:
    	if word not in non_dupes:
    		non_dupes.append(word)
    	else:
    		pass
    return non_dupes

print find_duplicates(words)


"""
Given a list of words, print the words in ascending order of length
Bonus: do it on a file instead of the list provided
Bonus: print the words in alphabetical order in ascending order of length
"""
def word_length(words):
    pass

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
