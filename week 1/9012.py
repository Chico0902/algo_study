# T = int(input())
# import re



# for i in range(T):
#     a = str(input())
#     while True : 
#         a=re.sub("\(\)","",a)
#         if a == None :
#             print('yes')
#             break
        
#         else :
#             print('no')
#             break
        
T = int(input())
import re

for i in range(T):
    a = str(input())
    while True:
        new_a = a  
        a = re.sub('\(\)', '', a)

        if not a:  
            print('yes')
            break
        elif a == new_a:
            print('no')
            break
