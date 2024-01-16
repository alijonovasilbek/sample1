
#vazifa1
# def tugrilash(s):
#     list1=[]
#     namuna= {')': '(', '}': '{', ']': '['}
#
#     for char in s:
#      if char in namuna.values():
#          list1.append(char)
#      elif char in namuna.keys():
#          if not list1 or list1.pop()!=namuna[char]:
#                return False
#
#      return not list1
# a=["[{1,2, (5,6)}]", "{)[]){}", "({[]})", "[()]", "{[()]}", "{[}"]
#
# for b in a:
#     natija=tugrilash(b)
#     print(f"{b}  --> {'togri' if natija else 'notogri'}")

#vazifa2
# def daraja(s):
#  d=0
#  for i in range(1,s+1):
#      d+=i
#  return d*d
#
# def kdaraja(l):
#     h=0
#     for k in range(1,l+1):
#         h+=k*k
#
#     return h
# print(f"yigindisining kvadrati {daraja(10)}")
# print(f"kvadratlarining yigindisi {kdaraja(10)}")
# farq=daraja(10)-kdaraja(10)
# print(f"{daraja(10)} - {kdaraja(10) } =={farq}")
#vazifa3
# a=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r' : '60'}]
# list1=[]
# for i in a:
#     dict1={key: int(value) for key , value in i.items()}
#     list1.append(dict1)
# print(list1)
# list2=[]
# for i in a:
#     dict1={key: float(value) for key , value in i.items()}
#     list2.append(dict1)
# print(list2)
#vazifa4
# a={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# for v in a.values():
#     v.clear()
# print(a)
#vazifa5
#
# a={'Matematika': [88, 89, 90], 'Fizika': [92, 94, 89], 'Kimyo': [90, 87, 93]}
# a["Matematika"]=list(map(lambda s:s+1 , a['Matematika']))
# a['Fizika']=list(map(lambda s:s-2, a['Fizika']))
# print(a)
#vazifa6
# fan=input("fanni kiriting masalan (Science) yoki (Math): ")
# z=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# list1=[]
# for i in z:
#     for k,v in i.items():
#         if k==fan:
#             list1.append(v)
# print(f" {fan}: {list1}")
#vazifa7
# a={1: 'qizil', 2: 'yashil', 3: 'qora', 4: 'oq', 5: 'qora'}
# dict1={}
# for k,v in a.items():
#     dict1[v]=len(v)
# print(dict1)
#vazifa8
# n= int(input('kalit index ni kiriting; '))
# num = {'physics': 80, 'math': 90, 'chemistry': 86}
# key=list(num.keys())
# print(f" {key[n]} ")
#
# a={'Theodore': 19, 'Roxanne': 20, 'Mathew': 21, 'Betty': 20}
# d=list(a.items())
# print(d)
# name = ['Snowball', 'Chewy', 'Bubbles', 'Gruff']
# animal = ['Cat', 'Dog', 'Fish', 'Goat']
# age = [1, 2, 2, 6]
# z=zip(name,animal,age)
# for name,animal,age in z:
#     print("%s  %s  %s" % (name, animal, age))
#
# fruits = {"apple", "banana", "cherry"}
# more_fruits = ["orange", "mango", "grapes"]
# fruits.update(more_fruits)
# # print(fruits)
# char=set("jklfdjkkje33")
# print(char)
#
# a=['foo', 'bar', 'abc', 'foo', 'qux', 'bar', 'baz']
# # print(set(a))
# a = [{'x': 10, 'y': 20, 'z': 30, 'p': 40, 'q': 50, 'r': 60}]
#
# # Sözlükleri 'x' anahtarına göre sırala
# sorted_a = sorted(a, key=lambda x: a[x], reverse=True)
#
# # print(sorted_a)
# n=input("matn kiriting; ")
# qisqartma=" "
# list1=n.split()
# for i in list1:
#      qisqartma+=i[0].upper()
# print(qisqartma)
# n=int(input("son kiriting; "))
# if type(n)==str:
#     print("kiritgan qiymatingiz son emas")
# else:
#    print(n)
# n=(input("son kiriting; "))
# try type(n)==int:
#   print(n)
# except
#      print("sz son kiritmadingiz; ")
#
# def tekshirish(a):
#   qator1=["qwertyuiop"]
#   qator2=["asdfghjkl"]
#   qator3=["zxcvbnm"]
#   list2=[ ]
#   qator1.split()
#   qator2.split()
#   qator3.split()
#
#   a.split(" ")
#   for i in a:
#       for j in i:
#          if j in qator1:
#              list2.append(i)
#          if j in qator2:
#               list2.append(i)
#          if j in qator3:
#               list2.append(i)
#   return list2
# sozlar = ["Salom","Alaska","Dada","Tinchlik"]
# print(tekshirish(sozlar))
# #
# a=tuple(input("sonlarini kiriting :"))
# iv=tuple(input("index va valueni kiriting; "))

#
# n=int(input("sonni kiriting; "))
# count=0
# list1=[]
# for i in range(1,n+1):
#    for j in range(2,int(((n/2)+1))):
#        if int(i%j)!=0:
#          list1.append(i)
# print(list1)

#
# a=(input("matn  kiriting; "))
# a.split()
# list1=[]
# for i in a:
#     if i.isdigit():
#      list1.append(i)
#
# print(sum(list1))

# def tub_sonlarni_aniqlash(n):
#     tub_sonlar = []
#     for son in range(2, n + 1):
#         tub = True
#         for i in range(2, int(son ** 0.5) + 1):
#             if son % i == 0:
#                 tub = False
#                 break
#         if tub:
#             tub_sonlar.append(son)
#     return tub_sonlar
#
# # Masalan, 100 gacha bo'lgan tub sonlarni olish:
# n = 100
# tub_sonlar = tub_sonlarni_aniqlash(n)
# print(f"1 dan {n} gacha bo'lgan tub sonlar: {tub_sonlar}")
# def tubsonlar(n):
#  tubson=[]
#  if n>1:
#     for num in range(2,n+1):
#         tubis=True
#         for son in range(2,int(num**0.5)+1):
#             if num%son==0:
#                 tubis=False
#                 break
#         if tubis:
#             tubson.append(num)
#  return    tubson
# print(tubsonlar(100))
#
# matn = "Kiritilgan matnda eng koʻp takrorlangan soʻz  eng eng va uni necha marta takrorlanganini chiqaruvchi dastur phytonda"
#
# sozlar = matn.split()
# takrorlanishlar = {}
#
# for soz in sozlar:
#     if soz in takrorlanishlar:
#         takrorlanishlar[soz] += 1
#     else:
#         takrorlanishlar[soz] = 1
#
# eng_ko_p_takrorlangan_soz = max(takrorlanishlar, key=takrorlanishlar.get)
# necha_marta = takrorlanishlar[eng_ko_p_takrorlangan_soz]
#
# print(f"Eng koʻp takrorlangan soʻz: {eng_ko_p_takrorlangan_soz}")
# print(f"{eng_ko_p_takrorlangan_soz} soʻzi {necha_marta} marta takrorlangan")












# import re
# if re.match("^[a-z]{15}([0-9]{3})[@][gmail][.]([a-z]{3})$","alijonovasilbek958@gmail.com"):
#
# import re
# if re.match("^([0-9]{3})\.([0-9]{1})\.([0-9]{1})\.([0-9]{3})$", "192.0.2.126"):
#     print("IPv4 to'gri ")
# else :
#     print("ipv xato")
#
# import re
# if re.match(" ^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}$","2001:0db8:85a3:0000:0000:8a2e:0370:7334"):
#     print("ipv6 togri ")
# else:
#     print("ipv6 xato")











