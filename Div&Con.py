def matricSearch(arr, l, r):
    if r-l > 1:
        mid = l + (r-l) // 2
        if arr[mid]-arr[mid-1] != 1:
            return (arr[mid]+arr[mid-1])/2
        if arr[mid]-arr[0] == mid:
            return matricSearch(arr, mid+1, r)
        else:
            return matricSearch(arr, l, mid)
    else:
        if arr[r]-arr[l] != 1:
            return (arr[r]+arr[l])/2
        else:
            return arr[l]-1


students = [1, 2, 3, 4, 5, 6, 8, 9, 10]
print("Student no.", int(matricSearch(students, 0, len(students)-1)), "is missing")
