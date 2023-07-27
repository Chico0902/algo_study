# T = int(input())

# my_list = list(range(1,T+1))
# while len(my_list) > 1 :

#     for i in range(T) :
        
#         if i % 2 == 0:
            
#             my_list[1:]
#         else :
#             my_list[1:] + list(my_list[:1])
            
# print(my_list)

# SyntaxError: name 'my_list' is used prior to global declaration 오류 발생

#_________________________________________________


T = int(input())

my_list = list(range(1,T+1))

while len(my_list) > 1:
    for i in range(len(my_list)):
        if i % 2 == 0:
            my_list = my_list[1:]
        else:
            my_list = my_list[1:] + my_list[:1]

print(my_list)