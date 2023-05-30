"""def solve(length,Arr):
    d = {}
    for i in Arr:
        d[i] = d.get(i,0) + 1
    if str(d.keys())=="dict_keys([0])":
        return 0
    Min = float("inf")
    for i in d.values():
        if i==length:
            return -1
        Min = min(Min,i)
    return length - Min"""
def estimate_num_liars(n, statements):
    min_upper_bound = n
    max_lower_bound = n - count_true(statements)

    for i, l in enumerate(statements):
        if l > max_lower_bound:
            return -1
        if n - l >= max_lower_bound:
            max_lower_bound = n - l + 1
        if n - l + 1 < min_upper_bound:
            min_upper_bound = n - l + 1

    return max(max_lower_bound, min_upper_bound)

def count_true(statements):
    return sum(1 for l in statements if l == 0)


tests = int(input(""))
while(tests>0):
    tests -= 1
    length = int(input(""))
    Arr = tuple(map(int, input("").split()))
    print(estimate_num_liars(length,Arr))


