def pattern(n):
    for i in range(n):
        print(' '* (n-i-1),end='')
        print("*" *(2*i+1))


n = int( input('Enter value for n: ') )
pattern(n)