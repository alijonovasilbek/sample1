#
#vazifa1
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
#
# result = [x + y for x in list1 for y in list2]
#
# print(result)
#vazifa2
# list1=["mike","","emma","kelly","","brad"]
# for i in list1:
#     if i=="":
#         list1.remove(i)
# print(list1)
# while "" in list1:
#     list1.remove("")
# print(list1)
# #vazifa3
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
#vazifa4
# list=[1,0,2,0,3,0,4]
# a=[]
# b=[]
# for i in list:
#     if i==0:
#         b.append(0)
#     else:
#         a.append(i)
# a.extend(b)
# print(a)
# #vazifa5
# blist = [10, 20, [30, 40], [50, 60, 70]]
# flist = []
#
# for i in blist:
#     if type(i) == list:
#         for j in i:
#             flist.append(j)
#     else:
#         flist.append(i)
#
# print(flist)lll
#

#
# print("yaqin do'stlaringiz ismini kiriting; ")
# ismlar=[]
# n=1
# while True:
#     savol=(f"{n} do/stingiz ismini kiiriting;;; ")
#     ism=input(savol)
#     ismlar.append(ism)
#     takrorlash=input("yana ism qushaszmi????(ha yo )")
#     n+=1
#     if takrorlash!='ha':
#         break
# print(ismlar)
# print("do'stlar yoshini saqlaymiz!!!")
# dostlar={}
# ishora=True
# while ishora:
#     ism=input("ismini kiriting; ")
#     yosh=input("yoshini kiritning  ")
#     dostlar[ism]=int(yosh)
#
#     javob=input("yana malumot qo'shasizmi?/ha yo")
#     if javob=='yo'  :
#        ishora=False
# for ism,yosh in dostlar.items():
#     print(f"{ism.title()} ,{yosh} yoshda")
# print(dostlar)
# #
# talabalar=['sardor', 'hasan', 'husan', 'olim']
# baholanganlar={}
# while talabalar:
#     talaba=talabalar.pop()
#     baho=input(f"{talaba}, ning bahosini kiriting;")
#     print(f"{talaba} baholandi")
#     baholanganlar[talaba]=int(baho)
# print(baholanganlar)
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# mylist=[x+y for x in list1 for y in list2]
# print(mylist)
#
# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
# for i in list1:
#     if i=="":
#         list1.remove(i)
# print(list1)
# a=""
# while a in list1:
#     list1.remove(a)
# # print(list1)
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# list1[2][2].append(7000)
# print(list1)
#
# list=[1,0,2,0,3,0,4]
# a=[]
# b=[]
# for i in list:
#     if i==0:
#         b.append(0)
#     else:
#         a.append(i)
# a.extend(b)
# print(a)
#
# k=[10, 20, [30, 40], [50, 60, 70]]
# bush=[]
# for i in k:
#     if type(i)==list:
#         for j in i:
#             bush.append(j)
#     else:
#         bush.append(i)
# print(bush)

#
# def ismyasa(ism,familiya,otsining_ismi=''):
#     if otsining_ismi:
#         tuliqism=f"{ism}, {familiya},{otsining_ismi}"
#     else:
#         tuliqism=f"{ism},{familiya}"
#     return tuliqism
# talaba=ismyasa('abror','dostov')
# print(talaba)

# def oraliq(min,max,qadam=None):
#     list=[]
#     if qadam:
#       while min<max:
#         list.append(min)
#         min += qadam
#       return list
#     else:
#         while min < max:
#             list.append(min)
#             min += 1
#         return list
# print(oraliq(3,45,3))

#
# def avto_info(kompaniya,model,rangi,korobka,yili,narhi=None):
#     avto={'kompaniya': kompaniya,
#           'model':model,
#           'rang':rangi,
#           'karobka':korobka,
#           'yil':yili,
#           'narhi':narhi}
#     return avto
# print("saytimizdagi avtolar ro'yxatini kiritamiz.")
# avtolar=[]
# while True:
#     print("\nQuyidagi malumotlarni kiriting;", end=" ")
#     kompaniya=input("ishlab chiqaruvchi : ")
#     model=input("model: ")
#     rangi=input("rangi: ")
#     karobka=input("korobka: ")
#     yili=input("yili ; ")
#     narhi=input("narhi; ")
#     avtolar.append(avto_info(kompaniya,model,rangi,karobka,yili,narhi))
#
#     javob =input("yana avto qushaszmi? (no/ yes)")
#     if javob=='no':
#         break
# print("\nsalondagi avtolar:")
# for avto in avtolar:
#     if avto['narhi']:
#         narhi=avto['narhi']
#     else:
#         narhi="nomalum"
#     print(f"{avto['rang'].title()} {model},{karobka} karobka. narh; {narhi}")
#
#
# a=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# s=[]
# for i in a:
#     if i%2==0:
#         s.append(i)
#
# print(s)


#
#
# color1 = ["Red", "Green", "Orange", "White"]
# color2 = ["Black", "Green", "White", "Pink"]
# k=[]
# for i in color1:
#      for j in color2:
#          if i==j:
#             k.append(i)
# print(k)
#
#
# a=[11, 33, 50]
# for i in a:
#     print(i, end="")
# obj={}
# for i in range(1,21):
#     obj[i]=[ ]
# print(obj)
# list1 = ['a','b','c','d','e','f']
# list2 = ['d','e','f','g','h']
# a=[]
# b=[]
# for i in list1:
#     if i not in list2:
#         a.append(i)
# list2.extend(a)
# for j in list2:
#     if j not in list1:
#         b.append(j)
# list1.extend(b)
# print(list2)
# print(list1)
#
# l=[[5*i+j for j in range(1,6)] for  i in range(7)]
# print(l)
#
# l = [(1, 2), (3, 4), (1, 2), (5, 6), (7, 8), (1, 2), (3, 4), (3, 4),
#  (7, 8), (9, 10)]
# o=[]
# for i in l:
#   if type(i)==tuple:
#    for j  in i:
#      o.append(j)
#   else:
#       o.append(i)
# h=[]
# for u in o:
#    if o.count(u)==1:
#     h.append(u)
# print(h)
# my_list = [{'key': {'subkey': 1}}, {'key': {'subkey': 10}}, {'key': {'subkey': 5}}]
# print("Original List: ")
# print(my_list)
#
# my_list.sort(key=lambda e: e['key']['subkey'], reverse=True)
# print("Sorted List: ")
# print(my_list)
# num1 = [1, 3, 5, 7, 9, 10]
# num2 = [2, 4, 6, 8]
# num1[-1:]=num2
# print(num1)
#
# x = [(4, 1), (1, 2), (6, 8)]
#
# min_element = x[0][1]  # Boshlang'ichda birinchi kortejni kichik elementi sifatida o'rnating
#
# for item in x:
#     if item[1] < min_element:
#         min_element = item[1]
#
# print("Ikkinchi indexdagi eng kichik element:", min_element)
#
#
# a=[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0 , 0, 2, 9, 7, 1]
# b=[]
# c=[]
# for i in a:
#     if i==0:
#         b.append(0)
#     else:
#         c.append(i)
# c.extend(b)
# print(c)
#
# a= [[1,2,3], [4,5,6], [10,11,12], [7,8,9]]
# print(max(a,key=sum))
# # my_list = [{},{},{}]
# my_list1 = [{1:2},{},{}]
# d=0
# f=0
# for i in my_list1:
#     if i:
#       d+=1
#     else:
#      f+=1
# if d>f:
#     print(False)
# else:
#     print(True)
# list1=[1,3,2]
# list2=list1*2
# print(list2)    #solution [1, 3, 2, 1, 3, 2]
# a='hello world'
# print([i.lower() for  i in a]) #solution ['h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

# a,b=[3,2,1],[5,4,6]
# s=a+b
# print(s)
# a.extend(b)
# print(a)       #solution [3, 2, 1, 5, 4, 6]

#
# list1=["a","b","c"]
# list2=list(map(lambda x : x.upper(),list1))
# print(list2)
#
# list1=[2,3,4,5,5]
# list2=[5,3,4,5,56,4]
# def add_d(x,y):
#     return x+y,x-y
#
# list3=list(map(add_d,list1,list2))
#
# print(list3)
#
# tuple1=('2','3','4','5')
# print(list(map(int,tuple1)))
# def fib(n):
#     if n<=0:
#         return None
#     if n==1:
#         return [1]
#     n1=1
#     n2=1
#     list1=[n1,n2]
#
#     for _ in range(n-2):
#         list1.append(n1+n2)
#         n1,n2=n2,n1+n2
#     return list1
#
#
# print(list(map(lambda x:x**2,fib(5))))

#
# k=[10, 20, [30, 40,[50,[80,5,6,7]]], [50, 60, 70]]
# list2=[]
# def rec_list(k):
#     for i in k:
#         if type(i)==list:
#             rec_list(i)
#         else:
#             list2.append(i)
#
# rec_list(k)
# print(list2)
# def fib(n):
#     if n==0:
#         return None
#     if n==1:
#         return [1]
#
#     n1=1
#     n2=1
#     list1=[n1,n2]
#     for _ in range(n-2):
#         list1.append(n1+n2)
#         n1,n2=n2,n1+n2
#     return list1
# print(fib(12))
# def suma(*sonlar):
#     yigindi=0
#     for son in sonlar:
#         yigindi+=son
#     return yigindi
# print(suma(1,2,3,4,5,5,6,4,5))
# def avtoinfo(kompaniya,model,**malumotlar):
#     malumotlar['kompaniya']=kompaniya
#     malumotlar['model']=model
#     return malumotlar
#
# avto1=avtoinfo("gm","malibu",rang='qora',yil=2013)
# print(avto1)

# def kopaytma(*sonlar):
#     s=1
#     for i in sonlar:
#         s*=i
#     return s
# print(kopaytma(3,5,6,7,7,8,8))
# def talabalar(ism,familiya,**malumotlar):
#     malumotlar['ismi']=ism
#     malumotlar['familiyasi']=familiya
#     return malumotlar
# a=talabalar("fam",'fksjf',rang='qora',yili='2222')
# print(a)
#
# import random as r
# #
# # son=r.randint(0,200)
# # print(son)
# x=list(range(23))
# print(x)
# r.shuffle(x)
# # print(x)
# import math
# uzunlik=lambda pi,r: 2*pi*r
# print(uzunlik(math.pi,10))
# kvadrat=lambda x,y:x**y
# print(kvadrat(4,3))

from math import sqrt
# sonlar=list(range(11))
# ildizlar=list(map(sqrt,sonlar))
# print(ildizlar)

# def daraja(n):
#     return n*n
#
# print(list(map(daraja,sonlar)))
#
# kvadratlar=list(map(lambda x:pow(x,2),sonlar))
# print(kvadratlar)
#
# dist={0:10,1:20}
# dist[2]=30
# print(dist)
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dict4={}
# for d in (dic1,dic2,dic3): dict4.update(d)
# print(dict4)
# n=int(input("sonni kiriting; "))
# dic1={1:10, 2:20,3:56}
# if n in dic1.keys():
#     print(f"lugatda {n} kalit bor")
# else:
#     print("yo")
# d = {'x': 10, 'y': 20, 'z': 30}
# s={}
# for k,v in d.items():
#     print(k,v)
# n=int(input("sonni kiriting;"))
# dic={}
# for i in range(1,n+1):
#     dic[i]=i*i
# print(dic)
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic2.update(dic1)
# print(dic2)
# d = {'x': 10, 'y': 20, 'z': 30}
# print(sum(d.values()))
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
#
# d=dic1.copy()
# d.update(dic2)
# print(d)
# keys = ['red', 'green', 'blue']
# values = ['#FF0000','#008000', '#0000FF']
# d=dict(zip(keys,values))
# print(d)
# if len(my_dict):
#     print("uzunlikka ega")
# else:
#     print("lugat bosh")

# test_dict = {"Gfg" : 5, "is" : 8, "Best" : 10, "for" : 8, "Geeks" : 9}
# updite={"Gfg":10,"Best":17}
# for sub in test_dict:
#     if sub in updite:
#         test_dict[sub]=updite[sub]
# print(str(test_dict))
# res={key: updite.get(key,test_dict[key]) for key in test_dict}
# print(res)
# dicPC = {"HP": 11, "Acer": 7, "Lenovo": 17, "Del": 23}
# dicPhone = {"Sumsung": 22, "Iphone": 9, "Other": 13}
# dicTablet = {"Sumsung": 15, "Other": 13}
# s={}
# for d in (dicPC,dicTablet,dicPhone): s.update(d)
# print(s)
# students = {"student_1" : 13 , "student_2" : 17 , "student_3" : 9 , "student_4" : 15 ,
# 			 "student_5" : 8 , "student_6" : 14 , "student_7" : 16 , "student_8" : 12 ,
# 			 "student_9" : 13 , "student_10" : 15 , "student_11" : 14 , "student_112" : 9 ,
# 			 "student_13" : 10 , "student_14" : 12 , "student_15" : 13 , "student_16" : 7 ,
# 			 "student_17" : 12 , "student_18" : 15 , "student_19" : 9 , "student_20" : 17 ,}
#
# student={k:v for k,v in students.items() if v>=10}
# print(student)
# n=int(input("sonni kiriitinng; "))
# dict={str(i): i*i for i in range(1,n+1)}
# print(dict)
# s = 'language'
# d={}
# for i in s:
#     d[i]=s.count(i)
#
# print(d)
# def jufttoq(l):
#     dictar=dict()
#     for s in l:
#         if s%2==0:
#             dictar[s]="pair"
#         else:
#             dictar[s]="impair"
#     return dictar
# l = [24 , 14 , 3 , 36 , 41 , 22 , 15]
#
# print(jufttoq(l))










