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