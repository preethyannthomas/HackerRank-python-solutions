def average(array):
    # your code goes here
    array = set(array)
    res = sum(array)/len(array)
    return res

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
