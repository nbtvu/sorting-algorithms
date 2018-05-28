def RadixSort(arr):
    def countingSort(arr, l, div):
        counts = [0] * 10
        for i in range(l):
            counts[arr[i] // div % 10] += 1
        for i in range(1, 10):
            counts[i] += counts[i - 1]
        output = [0] * l
        for i in reversed(range(l)):
            d = arr[i] // div % 10
            output[counts[d] - 1] = arr[i]
            counts[d] -= 1
        for i in range(l):
            arr[i] = output[i]
    l = len(arr)
    maxEle = max(arr)
    div = 1
    while maxEle//div > 0:
        countingSort(arr, l, div)
        div *= 10

a = [4, 2, 9, 1, 2, 7, 19, 8, 35, 26, 1, 1, 87, 22, 170, 45, 75, 90, 802, 24, 2, 66]
RadixSort(a)
print(a)
