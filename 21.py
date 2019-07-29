import statistics as st
count=int(input(" "))
ara=list(map(int,input().split()))
men=False
for i in range(1,count):
    l1=ara[:i]
    l2=ara[i:]
    if st.mean(l1)==st.mean(l2):
        men=True
if men==True:
    print("yes")
else:
    print("no")
