# vazifa1

# #
# def generatepascal(n):
#     qator=[]
#     for i in range(n):
#         if i==0:
#             qator.append([1])
#         else:
#             list1=[1]
#             for j in range(1,i):
#               list1.append(qator[i-1][j-1]+qator[i-1][j])
#             list1.append(1)
#             qator.append(list1)
#     return qator
# print(generatepascal(5))
# def printpascal(qator):
#     maxw=len(' '.join(map(str, qator[-1])))
#     for list1 in qator:
#         list1str=' '.join(map(str,list1))
#         print(list1str.center(maxw))
# n=int(input("Pascal uchburchagi qatorini kiriting; "))
# pascaluchburchak=generatepascal(n)
# printpascal(pascaluchburchak)
#vazifa2
# lugat=dict(x=list(range(11,20)),y= list(range(21,30)), z=list(range(31,40)) )
# print(lugat)
# print(lugat['x'][4])
# print(lugat['y'][4])
# print(lugat['z'][4])
# for k,v in lugat.items():
#     print(k,"ning qiymati",v)
#vazifa3
# a={'c1': 'Qizil', 'c2': 'Yashil', 'c3': None}
# a={k:v for (k,v) in a.items() if v is not None}
# print(a)
#vazifa4
# a={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# a={k:v for(k,v) in a.items() if  v>=170 }
# print(a)
#vazifa5
# a=['S001', 'S002', 'S003', 'S004']
# b=['Adina Park', 'Leyton Marsh', 'Dunkan Boyl', 'Saim Richards']
# c=[85, 98, 89, 92]
# d=[{t:{y:w} for (t,y,w) in zip(a,b,c)}]
# print(d)
#vazifa6
# a={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# filtereda={k:v for (k,v) in a.items() if v[0]>=6 and v[1]>=70 }
# print(filtereda)
#vazifa7
# n=int(input(" lugat qiymatlarini qaysi songa tekshirmoqchisiz; "))
# a={'Cierra Vega': 12, 'Alden Cantrell': 12, 'Kierra Gentry': 12, 'Pierre Cox': 12}
# d=all(value==n for value in a.values())
# if d:
#     print("True")
# else:
#     print("False")
#vazifa8
# a=[('sariq', 1), ('kok', 2), ('sariq', 3), ('kok', 4), ('qizil', 1)]
# bb={}
# for k,v in a:
#     if k in bb:
#         bb[k].append(v)
#     else:
#         bb[k]=[v]
# print(bb)
# list1=[{'id': '#FF0000', 'color': 'Red'}, {'id': '#800000', 'color': 'Maroon'}, {'id': '#FFFF00', 'color': 'Yellow'}, {'id': '#808000', 'color': 'Olive'}]
# a="FF0000"
# for i in list1:
#     for t,v in i.items():
#       if  v==a:
#           list1.remove(i)
#
# print(list1)

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
#
# sample={'name':"kelly", 'age':23,"salary":5555, "city":"new york"}
# keys=["name","salary"]
# dict1={}
# for i in keys:
#     dict1[i]=sample[i]
# print(dict1)
# #
# list1=["red", "green","black"]
# list2=list(map(list,list1))
# print(list2)
#
# def fib(n):
#     if n<=0:
#         return None
#     if n==1:
#         return [1]
#
#     n1=1
#     n2=1
#     list1=[n1,n2]
#     for _ in range(n-2):
#         list1.append((n1+n2))
#         n1,n2=n2,n1+n2
#     return list1
#
# n=int(input("son kiriting; "))
# list2=fib(n)
# print(list2)
#
#
#
#

#
#
# list1=[12,23,43,[12,12,43,54[23,232,55]],[23,55]]
#
# list2=[]
# def qaytar(list1):
#     for i in list1:
#         if type(i)==list:
#          qaytar(i)
#         else:
#             list2.append(i)
#
# qaytar(list1)
# # print(list2)
# list1=[('item1','12.22'),('item2','55.6')]
# print(sorted(list1, key=lambda s:s[1], reverse=True))
# def qaytar(satr):
#     qaytarilgan=''
#     for i in range(len(satr)-1,-1,-1):
#         qaytarilgan+=satr[i]
#     return qaytarilgan
# a=qaytar('mamlakat')
# # print(a)
start=int(input("boshlangich sonni kiriting; "))
end=int(input("oxirgi sonni kiriting; "))
for num in range(start,end):
 if num>1:
    isprime=True
    for i in range(2, int(num**0.5)+1):
            if num%i==0:
                isprime=False
                break
    if isprime:
     print("tub son")
    else:
        print("xato")


#









