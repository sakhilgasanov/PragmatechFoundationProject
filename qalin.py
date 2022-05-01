try:
    sayim=0
    qalinsesler=["a o u"]
    soz=(input("sozu daxil edin : "))
    for herf in soz:
        if herf in qalinsesler:
            sayim+=1
            print(sayim)  
            
except:
    print("eded daxil etmeyin!")