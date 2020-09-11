t = int(input())
while(t>0):
    n = int(input())
    arr  = list(map(int, input().split()))
    diff = []
    for i in range(n-1):
        diff.append(arr[i]+arr[i+1])
    print(diff)
