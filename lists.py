def find_subsets(arr):
    
    subsets= []
    subsets.append([])

    for value in arr:

        for i in range(len(subsets)):
            set = subsets[i].copy()
            set.append(value)
            subsets.append(set)

        return subsets
find_subsets([2, 4, 3, 0, 1])