def bin_search(A, b):
    # find the index of b in in array A. Let's say it returns i,
    # then A[i] <= b < A[i+i]
    left = 0
    right = len(A)
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] <= b:
            left = mid
        else:
            right = mid
        print(right, left)

    return left

def bin_search_other(A, b):
    # find the index of b in in array A. Let's say it returns i,
    # then A[i] < b <= A[i+i]
    left = 0
    right = len(A)
    while right - left > 1:
        mid = (left + right) // 2
        if A[mid] < b:
            left = mid
        else:
            right = mid
        print(right, left)

    return left

A = [0, 0, 0, 2, 2, 2, 3]
print(bin_search(A, 2))
print(bin_search_other(A, 1))