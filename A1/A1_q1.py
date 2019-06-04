
def pattern(n):
    for i in range(n):
        flag1=1
        for j in range(n):
            if n-1-j < i:
                print(max(n-j,n-i)+flag1,end=' ')
                flag1+=1
            else:
                print(max(n-i,n-j),end=' ')  
        print()
   

n = int( input('Enter value for n: ') )
pattern(n)