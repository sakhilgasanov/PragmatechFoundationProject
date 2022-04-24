#for n in range(42, 60, 3):
#    print(n, end=" ")

#for m in range(42, 60, 3):
#    print(m, end="\n")

#top=0
#for i in range(1, 11):
#    top+=i
#    print(top)


#for t in range(5, 10):
#    print(t)


#for z in range(10):
#    print(z)

#for q in range(16):
#    print("{0:3} {1:16}".format(q, 10**q))

#print("{}in {} masini var".format("Sahil", "yeni"))


#say=int(input("setir sayini daxil edin: "))
#for setir in range(1, say+1):
#    print("Setir |", setir)
    
    
#say=int(input("Setir sayini daxil edin : "))
#for setir in range(1, say+1):
#    for sutun in range(1, say+1):
#        olcu=setir*sutun
#        print(olcu, end=" ")
#    print()


#say=int(input("Setir sayini daxil edin : "))
#sayy=int(input("sutun sayini daxil edin : "))
#for setir in range(1, say+1):
#    for sutun in range(1, sayy+1):
#        deyer=setir*sutun
#        print(deyer, end="")
#    print()
    

say=int(input("Setir sayini daxil edin : "))
sayy=int(input("sutun sayini daxil edin : "))
for setir in range(1, say+1):
    for sutun in range(1, sayy+1):
        deyer=setir*sutun
        print("{0:4}".format(deyer), end="")
    print()