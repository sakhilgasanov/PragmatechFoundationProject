#n=0
#while n<=11:
#    n+=1
#    print(n)

#n=1
#deyer=int(input("eyeri daxil edin : "))
#while n<=deyer:
#   print(n)
#   n+=1


#deyer=False
#while not deyer:
#    giris = int(input("eded daxil edin : "))
#    if giris <= 150:
#        deyer = False
#    else: 
#        print(giris)


#yukseklik = int(input("agacin yuksekliyini daxil edin : "))
#setir = 0
#while setir < yukseklik:
#    saygac = 0 
#    while saygac < yukseklik - setir:
#        print(end=" ")
#        saygac += 1
#    saygac = 0
#    while saygac < 2*setir +1:
#        print(end="*")
#        saygac += 1
#    print()
#    setir +=1
    
derinlik=int(input("derinliyi daxil edin : "))
setir=0
while setir<derinlik:
    saygac=0
    while saygac<derinlik+setir:
        print(end=" ")
        saygac+=1
    saygac=0
    while saygac<2*setir+1:
        print(end="*")
        saygac+=1
    print()
    setir+=1