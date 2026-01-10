l=[1,39,67890,-67312,7,10,25,1,1,1,1,3]
print('The original list is',l)

count=0

for i in l:
    count += i

avg=count/len(l)

print('Sum =',count)
print('Average =',avg)

l.sort()

print('Smallest element is',l[0])
print('Largest element is',l[-1])