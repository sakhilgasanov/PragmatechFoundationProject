try:
    sayim=0
    qalinherfler=["a", "ı", "o", "u"]
    soz=(input("sozu daxil edin : "))
    for herf in soz:
        if herf in qalinherfler:
            sayim+=1
            print(sayim)
except:
    print("siz eded daxil etdiniz!")