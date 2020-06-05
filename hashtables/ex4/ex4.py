def has_negatives(a):
    """
    YOUR CODE HERE
    """
    positive_cache = {}
    negitive_cache = {}
    result = []

    for num in a:
        if num > 0 and num not in positive_cache:
            positive_cache[num] = num
        elif num < 0 and num not in negitive_cache:
            negitive_cache[num] = num

    for n in negitive_cache:
        key = abs(int(n))
        if key in positive_cache:
            result.append(positive_cache[key])

    return result

# could probably do it more efficiently and in a single iteration. First pass solution

if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))
