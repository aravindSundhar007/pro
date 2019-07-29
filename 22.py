count=int(input(" "))
ara=list(map(int,input().split()))
ara.sort(reverse=True)
#print(arr)
sum=0
sum1=0
result1=[]
for i in range(0,count,2):
    sum=sum+ara[i]
for j in range(1,count,2):
    sum1=sum1+ara[j]
result1.append([sum,sum1])
#print(res)
for i in result1:
    print(i[0] if i[0]>i[1] else i[1])
