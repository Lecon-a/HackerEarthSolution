def intersection(arr1, arr2, arr3, n1, n2, n3):
    x_loc = y_loc = z_loc = 0
    res = []
    while x_loc != n1 and y_loc != n2 and z_loc != n3:
        x = arr1[x_loc]
        y = arr2[y_loc]
        z = arr3[z_loc]

        if x == y and y == z:
            res.append(x)
            x_loc += 1
            y_loc += 1
            z_loc += 1
        elif x <= y and x <= z:
            x_loc += 1
        elif y <= x and y <= z:
            y_loc += 1
        else:
            z_loc += 1

    return res

n1 = int(input("Enter the size of the array: "))    
n2 = int(input("Enter the size of the array: "))    
n3 = int(input("Enter the size of the array: ")) 
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 3, 4, 5, 8]
arr3 = [1, 2, 5, 7, 9]   

print(f'The intersection of three arrays is ({intersection(arr1, arr2, arr3, n1, n2, n3)})')