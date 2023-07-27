# 이거 안쓰면 시간초과됨
import sys

input = sys.stdin.readline
# --------------------------------------------
# 함수 정의
list_X = []
def push_x(num) :
        list_X.append(num)
        
def pop_f_x():
    global list_X 
    if list_X == []:
        print(-1)
    else : 
        print(list_X[0])
        list_X = list_X[1:]

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

# 인풋 실행부분

list_X = []
for i in range(T):
    a = list(input().split())
    if a[0] == 'push':
        push_x(a[1])

    if a[0] == 'pop':
        pop_f_x()

    if a[0] == 'size':
        size_x()

    if a[0] == 'empty':
        empty_x()

    if a[0] == 'front':
        front_x()

    if a[0] == 'back':
        back_x()