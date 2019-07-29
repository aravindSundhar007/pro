inpu=int(input(" "))

d=0

xy=0

b=[]

while d<90 and d<inpu:

  s=0

  for j in str(inpu-d):

    s+=int(j)

  if s+(inpu-d)==inpu:

    xy+=1

    b.append(inpu-d)

  d+=1

print(xy)

for i in b:

  print(i)
