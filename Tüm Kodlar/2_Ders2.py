# -*- coding: utf-8 -*-
"""
Created on Mon Oct 17 17:07:25 2022

@author: SerdarKR
"""

#%%
a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

sonuc=a==b
print(bool(""))
print(bool(-1))

print(bool("Hello"))
print(bool(15))

print(bool(" "))

metin=" "
print(bool(metin.strip()))

bool([])
bool(["apple", "cherry", "banana"])

#%%operatorler
print(20//3)

print(5%2)
print(2**3)


x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
x[0]="a"
print(z[0])

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y
xx=5
yy=xx
yy=10
print(xx)

x = ["apple", "banana"]

print("banana" in x)

m1="Serdar kr"
print("kr" in m1)
print("serdar" in m1)#case sensitive

s1=21
s2=~s1
print(s2)

s1=5
s1=s1>>2

#%%listeler

list1=["dsdf",544,"sfsdf"]

list2=["ada",list1]
print(list2[1][1])

list1[1]=33

list2[1][1]=55
m1="sdfsdfs"
print(len(m1))
print(len(list2))
print(type(list2[1]))
print(len(list2[1]))

print(list1[-1])
print(list1[:])
print(list1[:-1])
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])

thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")

thislist = ["apple", "banana", "cherry"]

thislist[1:2] = ["blackcurrant", "watermelon"]

print(thislist)

thislist = ["apple", "banana", "cherry"]

for x in list2:
    for y in x:
        print(y)

mylist = ["apple", "banana", 45]

thislist = ["apple", mylist, 22]
for x in thislist:
    if type(x)==list:
        for y in x:
            print(y)
    else:
        print(x)

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])
  
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1
  
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)

list3=[23,"sdfs",567,89,"sdfd"]

list4=[x for x in list3 if type(x)==int]

liste5=[x for x in range(10)]
liste6=[x for x in range(10) if x%2==0]


liste6=[x for x in range(10) if x%2!=0]

liste7=[x for x in range(0,10,2)]


fruits = [" apple ", " banana ", "cherry", "kiwi", "mango"]

newlist = [(x.strip()).capitalize() for x in fruits]

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x if x != "banana" else "orange" for x in fruits]

print(newlist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)


def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]

thislist.sort(key = myfunc)

print(thislist)



thislist = ["apple", "banana", "cherry"]
mylist = thislist
thislist[0]=23
print(mylist)


#%%tuple lar

thistuple = ("apple", "banana", "cherry")
print(thistuple[0])
#thistuple[0]=45

thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))

#unpack tuple
fruits = ("apple", "banana", "cherry")

(green, yellow, red) = fruits

print(green)
print(yellow)
print(red)


fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")

(green, yellow, *red) = fruits

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
thisset = {"apple", "banana", "cherry"}
#print(thisset[0])
for x in thisset:
    print(x)

sehirler={"Düzce","Ankara","istanbul"}
thisdict = {
  0: "Ford",
  "model": "Mustang",
  "şehirler": sehirler
}
for x in thisdict["şehirler"]:
    print(x)

print(thisdict["şehirler"])

x = thisdict.keys()

xval = thisdict.values()
thisdict["year"] = 2020
y=x = thisdict.items()


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
for x, y in thisdict.items():
  print(x, y)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = dict(thisdict)
print(mydict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)



myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

for x,y in myfamily.items():
    print(x)
    for xx,yy in y.items():
        print(xx,yy)
















