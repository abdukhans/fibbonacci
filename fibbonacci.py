n      = int (input ('Enter Num:'))

first  = 1 

second = 1 
for i in range (n):
    if i == 0 :
        print (first)
    elif i == 1:
        print (second)
    else:
        new_num = first + second
        print (new_num)

        first = second
        second = new_num
