T = int(input())

my_list = list(range(1,T+1))
while len(my_list) == 1 :
    global my_list
    for i in range(T) :
        if i % 2 == 0:
            my_list[1:]
        else :
            my_list[1:] + list(my_list[:1])
            
print(my_list)