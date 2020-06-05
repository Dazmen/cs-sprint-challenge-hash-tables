# Your code here



def finder(files, queries):
    """
    YOUR CODE HERE
    """
    result = []
    paths_cache = {}

    for path in files:
        key = path.split('/')[-1]

        if key not in paths_cache:
            paths_cache[key] = []

        paths_cache[key].extend([path])

    for file in queries:
        if file in paths_cache:
            result.extend(paths_cache[file])
    # minimal performance difference between arr1 + arr2 and arr1.extends(arr2)

    print(result)
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
