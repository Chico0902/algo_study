import sys

input = sys.stdin.readline


list_X = []

def push_f_x(num) :
        list_X.insert(0,num)


def push_b_x(num) :
        list_X.append(num)
        
def pop_f_x():
    global list_X 
    if list_X == []:
        print(-1)
    else : 
        print(list_X[0])
        list_X = list_X[1:]
        


def pop_b_x():
    if list_X == []:
        print(-1)
    else : 
        print(list_X.pop())
       

def size_x():
    print(len(list_X))

def empty_x() :
    if list_X == []:
        print(1)
    else :
        print(0)

def front_x(): 
    if list_X == []:
        print(-1)
    else :
        print(list_X[0])

def back_x(): 
    if list_X == []:
        print(-1)
    else :
        print(list_X[-1])

T = int(input())

list_X = []
for i in range(T):
    a = list(input().split())
    if a[0] == 'push_front':
        push_f_x(a[1])
        
    if a[0] == 'push_back':
        push_b_x(a[1])

    if a[0] == 'pop_front':
        pop_f_x()    

    if a[0] == 'pop_back':
        pop_b_x()

    if a[0] == 'size':
        size_x()

    if a[0] == 'empty':
        empty_x()

    if a[0] == 'front':
        front_x()

    if a[0] == 'back':
        back_x()