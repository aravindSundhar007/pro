s=int(input(" "))
mist=list(map(int,input().split()))
mist.sort()
sin=0
se=0
for i in range(len(mist)):
    if mist[i]>=sin:
        se=se+1
    sin=sin+mist[i]
print(se)
