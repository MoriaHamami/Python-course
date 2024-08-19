def allSumsDP(arr):
    sums = set()
    # Not choosing any number results in sum zero
    sums.add(0)
    # Go over each number in array
    for num in arr:
        new_sums = set()
        # Add the number to each sum ("set" doesn't save duplicates)
        for sum in sums:
            new_sums.add(sum + num)
        sums.update(new_sums)
    return sums