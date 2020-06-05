def intersection(arrays):
    """
    YOUR CODE HERE
    """
    number_cache = {}
    result = []

    for arr in arrays:
        for num in arr:
            if num not in number_cache:
                number_cache[num] = 1
            else:
                number_cache[num] += 1

    for num in number_cache:
        if number_cache[num] == len(arrays):
            result.append(int(num))

    return result

# Test pass, not optimal solution. Does not account for potential dups.
# could implement a temp cache in nested loop to keep track of iterated nums, if num is in temp_cache, ignore it. This would help elimate false positives OR false negitives (with the numCount == len(arrays) statement)

if __name__ == "__main__":
    arrays = []

    arrays.append(list(range(1000000, 2000000)) + [1, 2, 3])
    arrays.append(list(range(2000000, 3000000)) + [1, 2, 3])
    arrays.append(list(range(3000000, 4000000)) + [1, 2, 3])

    print(intersection(arrays))
