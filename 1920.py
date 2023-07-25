#1920 문제

# 시간 초과로 틀림

# T = int(input())

# A = list(map(int,input().split()))

# S = int(input())

# B = list(map(int,input().split()))

# for i in range(S):
#     if B[i] in A:
#         print(1)
#     else :
#         print(0)

# ----------------------------------------------

# 다시 풀기

# 인풋들 받기

T = int(input())

A = list(map(int,input().split()))

S = int(input())

B = list(map(int,input().split()))


#바이너리 위해서 정렬 (함수내에서 .sort사용하면 시간초과)

new_A = sorted(A)

# 바이너리 함수(긁어옴..)

def binary_search(target, data):
    
    start = 0
    end = len(data) - 1

    while start <= end:
        mid = (start + end) // 2

        if data[mid] == target:
            return mid # 함수를 끝내버린다.
        elif data[mid] < target:
            start = mid + 1
        else:
            end = mid -1

    return None

# 결과 도출

for i in range(S):
    res = binary_search(B[i],new_A)
    if res == None :
        print(0)
    else :
        print(1)

