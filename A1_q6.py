def find_second_max(l):
	number_list = l
	maxItem = max(number_list)
	maxIndex = number_list.index(maxItem)
	secondMax=0
	for index in range(len(number_list)):
	    if(index != maxIndex):
	        secondMax = max(number_list[index],secondMax) 
	return secondMax
	
list_number = [1,2,3,4,3,6]
secondMax = find_second_max(list_number)
print(secondMax)