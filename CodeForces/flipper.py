num_cases = int(input())
while num_cases > 0:
    num_cases -= 1
    size = int(input())
    
    arr = list(map(int, input().split()))
    
    result = []
    is_flag = 0
    position = size + 1
    
    for i in range(size):
        if arr[i] == size:
            result.append(arr[i])
            position = i
        elif i > position:
            result.append(arr[i])
    
    if position == size - 1:
        answer = position - 1
        while arr[answer] >= arr[0] and answer >= 0:
            result.append(arr[answer])
            answer -= 1
        
        for i in range(answer + 1):
            result.append(arr[i])
    else:
        result.append(arr[position - 1])
        answer = position - 2
    
        while arr[answer] >= arr[0] and answer >= 0:
            result.append(arr[answer])
            answer -= 1
        
        for i in range(answer + 1):
            result.append(arr[i])
    
    for i in range(size):
        print(result[i], end=" ")
    
    print()