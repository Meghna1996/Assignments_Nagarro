from functools import reduce

#function for getting words in a list from a file
def words_file(filename):
	list_of_words = []
	with open(filename,'r') as f:
	    for line in f:
	        for word in line.split():
	            list_of_words.append(word)
	return list_of_words            


def upper_words(item):
    return item.upper()


#function for getting those words that doesn't contain 'a'
def filter_a(item):
    if 'a' in item:
        return False
    return True


filename = input('Enter filename: \n')

#printing the words of data in a file
list_of_words = words_file(filename)
print(list_of_words)

#printing the upper case of the words in a list using map
new_list = list(map(upper_words,list_of_words))
print(new_list)

#printing the list of words that doesn't contain 'a'
new_list2 = list(filter(filter_a ,list_of_words))
print(new_list2)

#printing the concatenation of strings using reduce
string_of_words = reduce(lambda str1, str2: str1 + str2,list_of_words)
print(string_of_words)