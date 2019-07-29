def Long(arr,size):
    result=[]
    count=1
    for i in range(0,size-1):
        if arr[i]<arr[i+1]:
            count+=1
        else:
            result.append(count)
            count=1
    result.append(count)
    print(max(result))
size=int(input())
arr=list(map(int,input(" ").split(" ")))
Long(arr,size)
