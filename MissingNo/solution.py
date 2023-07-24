def missingNo(n, arr):
    res = n * (n + 1)/2
    array_sum = 0
    for i in range(n-1):
        array_sum += arr[i]
    res = res - array_sum

    return int(res)

n = int(input("Array size: "))
arr = list(map(int, input("Enter array: ").split()))

output = missingNo(n, arr)
print(f'Missing value is {output}')