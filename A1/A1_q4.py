
def permutation_string(list1,k,n,old_str):
    if k == 0:
        print(old_str)
        return
    for i in range(n):
        final_str= old_str+ str(list1[i])
        permutation_string(list1,k-1,n,final_str)


list1 = []
n = int(input('Enter number of characters: '))
print('Enter the characters: ')
for i in range(n):
	list1.append(input())
k = int(input('Enter value for k: \n'))	

permutation_string(list1,k,n,'')