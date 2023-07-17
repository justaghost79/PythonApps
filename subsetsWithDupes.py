def find_subsets(arr):
    list.sort(arr)
    subsets = []
    subsets.append([])
    end_index = 0

    for i in range(len(arr)):
        start_index=0

        if i > 0 and arr[i] == arr[i-1]:
            start_index = end_index + 1
        end_index = len(subsets) -1

        for j in range(start_index, end_index+1):

            set = list(subsets[j])
            set.append(arr[i])
            subsets.append(set)

        return subsets
    
find_subsets([8,4,4])