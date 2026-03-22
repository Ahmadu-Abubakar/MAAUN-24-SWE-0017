import random

print("=== Candidate Score System ===")

# generate 10 random scores
scores = [random.randint(0, 100) for _ in range(10)]

# implementing merge sort
def merge_sort(arr):
    # base case
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    return merge(left_sorted, right_sorted)

# merging 
def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

sorted_scores = merge_sort(scores)
print("Sorted scores:", sorted_scores)

# binary search
def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid

        elif arr[mid] < target:
            left = mid + 1

        else:
            right = mid - 1

    return -1



# Asking user for a target
target = int(input("Enter score to search: "))

index = binary_search(sorted_scores, target)


# printing search result
index = binary_search(sorted_scores, target)

if index != -1:
    print("Score found at index:", index)
else:
    print("Score not found.")