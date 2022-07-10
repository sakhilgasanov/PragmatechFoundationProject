#tuple_a = 1, 2
#tuple_b = (1, 2)
#print(tuple_a == tuple_b)
#print(tuple_a[1])



#n = 5
#while n > 0 :
#    print(n)
#print('All done')


"""İstifadəçidən 2 ədəd alin ve bu iki ədəd arasindaki sadə ədədlərin ortalamasını print etdirin."""

eded_1=int(input('Birinci ededi daxil edin: '))
eded_2=int(input('Ikinci ededi daxil edin: '))

cem=0
for i in range(eded_1, eded_2+1):
    bolen_sayi=0
    say=0
    for j in range(1, i+1):
        if i%j==0:
            bolen_sayi+=1
            say+=1
    if bolen_sayi<=2:
        cem+=i
print(say)