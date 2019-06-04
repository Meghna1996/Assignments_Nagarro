def pattern(n):
    
    for i in range(n):
        ch= 'A'
        print(' '*(n-i),end='')
        num=2*i+1
        for j in range(num):
            print(ch,end='')
            if j<num//2:
                ch = chr(ord(ch)+1)
            else:
                ch=chr(ord(ch)-1)
        print()


n = int( input('Enter value for n: ') )
pattern(n)