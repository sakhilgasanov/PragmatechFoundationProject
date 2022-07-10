###########################################################
"""
x və y ədələri daxil edilir və bu ədələrin yeri dəyişdirilir
Yəni x=10 y=20 isə x=20 y=10 edilir
"""
#x=int(input('x ededini daxil edin: '))
#y=int(input('y ededini daxil edin: '))
#print('y=', x)
#print('x=', y)

############################################################
"""
print("123" + "abc")=?
"""
#print("123"+"abc")
#dırnaq içərisində yazıldığı üçün birləşdirir

############################################################

""" x = int(98.6)=? """

#x=int(98.6) tam hissəsini verir
#x=float(98.6) tam və kəsr hissəsini bir yerdə verir
#print(x) sualda print yazılmamışdı, əgər print yazılmasa heç bir nəticə olmazdı

############################################################

""" print((3 == 4)==0) kodun nəticəsi nə olacaq? """
# 3=4 true verir, true ilə true elə true verir

#############################################################

""" İstifadəçidən çevrənin radiusunu alın və uzunluğunu hesablayın. """
#r=float(input('Cevrenin uzunlugunu daxil edin: '))
#p=3.14
#l=2*p*r
#print(l)

##############################################################

""" Aşağıda verilmişlərdən hansılar Python-da keyword-dür?
 list, dict, or, if
"""
# hamısı rezerv sözlərdir

##############################################################

""" 
Aşağıdakı kodun nəticəsində ekrana nə çıxacaq?
x = 0
if x < 2 :
    print('Small')
elif x < 10 :
    print('Medium')
else :
    print('LARGE')
print('All done')

"""
#x = 0
#if x < 2 :
#    print('Small')
#elif x < 10 :
    #print('Medium')
#else :
#    print('LARGE')
#print('All done')

# birinci şərt ödəndiyi üçün small yazısı ekrana çıxacaq və sonda şərtdən asılı olmadan all done sözü çıxacaq

#################################################################

"""
Aşağıdakı kodun nəticəsində ekrana nə çıxacaq?
tot = 0 
for i in [5, 4, 3, 2, 1] :
    tot = tot + 1
print(tot)

"""

#tot = 0 
#for i in [5, 4, 3, 2, 1] :
#    tot = tot + 1
#print(tot)

# sayını verir

###################################################################

""" 5-ə bölünən və 30-dan kiçik ədədləri print etdirin. """

#eded=30
#for eded in range(1, eded):
#    if eded%5==0:
#        print(eded)

###################################################################

"""
10.	Deyək ki, bir string var, məsələn S='Natiq'. 
Bunun içində tapın ki, hər hərfdən neçə dənədir(dictionary formatında print edin). 
{N:1, a:1} və s. şəkildə.

"""

#soz='Natiq'

###################################################################

""" 11.	İstifadəcinin daxil etdiyi ədədin təkmi cütmü olduğunu print etdirin. """

#eded=int(input('Ededi daxil edin: '))
#if eded%2==0:
#    print('Eded cut ededdir')
#else:
#    print('Eded tek ededdir')

####################################################################

"""12.	İstifadəçidən bir ədəd alın ve 1-dən bu ədədə qədər olan tək ədədləri bir, cüt ədədləri də bir toplayin. 
Sonda hər iki nəticənin print etdirin. print edərkən format() metodundan istifadə edin.
"""
#eded=int(input('Ededinizi daxil edin: '))
#cem_tek=0
#cem_cut=0
#for i in range(1, eded):
#    if i%2==1:
#        cem_tek=cem_tek+i
#    else: 
#        cem_cut=cem_cut+i
#print(cem_tek)
#print(cem_cut)

#####################################################################

"""13.	İstifadəçidən bir string alın və içərisindəki rəqəmləri print etdirin.
 İnput:
 s=”a1d4d4d”
 Output:
 1 4 4
"""

#ifade=str(input('Ifadeni daxil edin:'))
#ededler=[]
#for reqem in ifade.split():
#    if reqem.isdigit():
#        ededler.append(int(reqem))
#    print(ededler)

####################################################################

"""
İstifadəcinin daxil etdiyi ədədin təkmi cütmü olduğunu print etdirin. 
Əgər təkdirsə kvadratını, cütdürsə 5-ə bölünməsindən alınan qalığı print etdirin
"""

#eded=int(input('Ededi daxil edin: '))
#if eded%2==1:
#    print("Eded tekdir", eded*eded)
#else:
#    bolunme=eded/5
#    kesr=float(bolunme-round(bolunme))
#    print("Eded cutdur", format(kesr))

#####################################################################

"""19.	0-dan 100-ə qədər cüt ədədləri toplayın, amma bunu while ilə edin"""
#cem=0
#for i in range(0, 101):
#    if i%2==0:
#        cem=cem+i
#print(cem)


#a=1
#cem=0
#while 1<=a<=100:
#    a+=1
#    if a%2==0:
#        cem=cem+a
#print(cem)

#######################################################################

"""21.	İkirəqəmli ədəd daxilir edilir və əgər rəqəmləri bərabərdirsə ekrana “=”, əks halda heç nə yazdırılır.
İnput: 33                                                                 Output :=
"""

#eded=int(input('Ikireqemli eded daxil edin: '))
#if eded.index(0)==eded.index(1):
#    print("=")

######################################################################

"""22.	Daxil edilən n ədədinin 5-ə bölünməsindən alınana qalığı ekrana yazdırın.
İnput: 26                                                                 Output: 1
"""

#eded=int(input('Ededi daxil edin: '))
#bolunme=eded/5
#qaliq=bolunme%1
#print(qaliq)

#########################################################################

"""
23.	Aşağıdakı yazılışlardan doğru və ya yanlış olanları qarşısına qeyd edin.
a=Natiq-yanlış          1 a=5-yanlış
b=”5”doğru             a1=5-doğru
c=’4’-doğru               d=’book’s’ yanlış
b=5 -doğru               c=’45.2’ doğru

"""

#######################################################################

for i in range(1, 10, 2):
    if i%5 == 0:
        print("Bingo!")
        break
else:
    print(i)
