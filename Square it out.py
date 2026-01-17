Start_range=int(input('Please enter the START of your range:  '))
End_range=int(input('Please enter the END of your range:  '))

Total_List=[]
Odd_List=[]
Even_List=[]

for i in range(Start_range,End_range+1):
    x=i*i
    Total_List.append(x)

for a in range(len(Total_List)):
    if Total_List[a]%2==0:
        b=a
        Even_List.append(b)
    else:
        Odd_List.append(a)

print('Squaring all the numbers within your range, we get',Total_List[:])
print('All the even square numbers are',Even_List[:])
print('All the odd square numbers are',Odd_List[:])