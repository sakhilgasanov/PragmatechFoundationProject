try:
    a=int(input("deyeri daxil edin: "))
    if a>0:
        print("deyer mwsbetdir")
    elif a<0:
        print("deyer menfidir")
    else:
        print("deyer sifirdir")
except:
    print("siz eded daxil etmemisiniz")