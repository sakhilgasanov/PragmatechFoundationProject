#l=[i for i in range(1000)]
#print(l)

"""l=[[2, 4, 6], 
   [3, 5, 7],
   [10, 11, 12]]

l_tam=[z for i in l for z in i]
print(l_tam)"""

""""l=[[2, 4, 6], 
   [3, 5, 7],
   [10, 11, 12]]

l_cut=[z for i in l for z in i if z%2==0]
print(l_cut)"""

phone_number=int(input('Enter the phone number: '))

t={}
for i in phone_number:
    0,1,2,3,4,5,6,7,8,9==int(i)
    if i not in t.keys():
        t[i].append
print(t)        