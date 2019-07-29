in=int(input(" "))

i=0

xy=0

b=[]

while i<90 and i<in:

  s=0

  for j in str(in-i):

    s+=int(j)

  if s+(in-i)==in:

    xy+=1

    b.append(in-i)

  i+=1

print(xy)

for i in b:

  print(i)
