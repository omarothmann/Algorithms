def find(arr):
    arr.sort()
    for x in range(0, len(arr)):
        if arr[x + 1] - arr[x] != 1:
            print("the missing student is: " ,(arr[x] + 1))
            arr.append(arr[x] + 1)
            arr.sort()
            # print(arr)

# find([1,2,4,5,6,7])
# find([7,5,4,3,2,1])
find([5,3,4,6,9,1,10,11,12,14,15,16])