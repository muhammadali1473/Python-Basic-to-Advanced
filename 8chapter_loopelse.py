'''

sum (1) = 1
sum(2)= 2
sum(3)= 3
sum(4)= 4
sum(5)= 5
sum(6)= 6
sum(7)= 7
'''

def sum(n):
    if(n==1):
        return 1
    return sum(n-1) + n
print(sum(4))
    