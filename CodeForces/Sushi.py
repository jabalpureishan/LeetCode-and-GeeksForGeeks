Test = int(input())
Input = list(map(int, input().split()))
Array = [1] * 100001
B, C, Result = 0, 0, 0
for i in range(1, Test):
    if Input[i] == Input[i-1]:
        Array[B] += 1
    else:
        B += 1
for i in range(1, B+1):
    if Array[i] == Array[i-1]:
        C = 2 * Array[i]
        Result = max(Result, C)
    elif Array[i] > Array[i-1]:
        C = 2 * Array[i-1]
        Result = max(Result, C)
    else:
        C = 2 * Array[i]
        Result = max(Result, C)
print(Result)

