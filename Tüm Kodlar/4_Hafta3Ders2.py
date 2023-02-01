# -*- coding: utf-8 -*-
"""
Created on Mon Oct 24 18:15:41 2022

@author: SerdarKR
"""

#%%fonksiyonlar

def fonk():
    pass

fonk()

def fonk1():
    print("fonk basladi")
fonk1()

def fonk2():
    return 5
i= fonk2()

def fonk3():
    return "serdar"

j=fonk3()

def fonk4(p1,p2):
    """
 alınan p1 ve p2 parametrelerinin çarpımını geri döner

    """
    return p1*p2

fonk4()

print(fonk4(1,2))  

def fonk5(p1,p2=1):
    return p1*p2

fonk5()
fonk5(9)
fonk5(9,9)


def fonk6(a,b,*c):
    print(c[0])

fonk6(1,2,3,4,5)

def fonk7(a,b,*c,d=26):
    print(c[0])
    print(d)

fonk7(1,2,3,4,5,6,7)
def fonk8():
    return[5,6,"serdar"]

x,y,z=fonk8()
print(x,"-",y,"-",z)

#lambda expression

fonk9= lambda x:x*3
fonk10=lambda x,y:x*y

xx=fonk9(9)

yy=fonk10(3,5)


#%%map kullanımı
def myfunc(a, b):
  return a + b

x = map(myfunc, ('apple', 'banana', 'cherry'), ('orange', 'lemon', 'pineapple'))
print(x)
print(list(x))






















