#try:
#    a=int(input("a ededini daxil edin: "))
#    b=int(input("b ededini daxil edin: "))
#    emeliyyat=input("emeliyyati daxil edin: ")
#   if emeliyyat=="+":
#       print(a+b)
#    elif emeliyyat=="-":
#         print(a-b)
#    elif emeliyyat=="*":
#        print(a*b)
#    elif emeliyyat=="/":
#        print(a/b)
#    else:
#        print("daxil etdiyiniz emeliyyat duzgun deyil")
#except:
#   print("siz eded daxil etmemisiniz")
    
    
def Toplama(a,b):
    print(a+b)
def Cixma(a,b):
    print(a-b)
def Vurma(a,b):
    print(a*b)
def Bolme(a,b):
    print(a/b)
try:
    a=int(input("a ededini daxil edin: "))
    b=int(input("b ededini daxil edin: "))
    emeliyyat=input("emeliyyati daxil edin: ")
    if emeliyyat=="+":
        Toplama(a,b)
    elif emeliyyat=="-":
        Cixma(a,b)
    elif emeliyyat=="*":
        Vurma(a,b)
    elif emeliyyat=="/":
        Bolme(a,b)
    else:
        print("daxil etdiyiniz emeliyyat duzgun deyil")
except:
    print("siz eded daxil etmemisiniz")