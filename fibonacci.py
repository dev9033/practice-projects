num = int(input('enter a number: '))
a, b = 0, 1
if (num == a) or (num == b):
    print("it's Fibonacci")
else:
    while True:
        c = a+b
        a, b = b, c
        if (num == b):
            print("it's Fibonacci")
            break
        elif num < b:
            print("it's not Fibonacci")
            break


# fibonacci number generator
# a,b = 0,1
# for i in range(100):
#     c = a+b
#     a,b=b,c
# print(b) 
