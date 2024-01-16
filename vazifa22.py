#vazifa1
# a=[2,3,45,66,66]
# b=[5,4,5,6,7,7]
# c=list(map(int, a+b))
# print(c)

#vazifa2
# list1 = {'razmerlar': [88, 89, 62, 95], 'razmerlar2': [77, 78, 84, 80]}
# print(dict(list1))
# list2 = list(map(lambda *x: dict(zip(list1, x)), *list1.values()))
# print(list2)
#vazifa3
# a=['salom','hello','world']
# j=list(map(list,map(list,a)))
# print(j)
# # vazifa4
# list1=[('salom','hello'),('hayr','goodbye'),('section','qism')]
# a=list(map(lambda v: ' '.join(v),list1))
# print(a)
#
# mx=lambda x,y:x if x>y else y
# print(mx(8,5))
#
# n=[3,45,5,6]
# print(list(map(lambda x:x**2,n)))
# print(list(filter(lambda s:s>5,n)))
#
# a=[3,3,4,5,6,6]
# b=[3,3,4,5,6,6]
# d=[3,3,4,5,6,6]
# print(list(map(lambda x,y,z:x+y+z,a,b,d)))
#
# a=[10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
# b=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list(map(lambda x,y:pow(x,y),a,b)))
# def change(s):
#     return str(s).upper(),str(s).lower()
#
#
# def fib(n):
#     if n<=0:
#         return None
#     if n==1:
#         return  [1]
#
#     n1=1
#     n2=1
#     list1=[n1,n2]
#     for _ in range(n-2):
#         list1.append(n1+n2)
#         n1,n2=n2,n1+n2
#     return list1
# n=int(input("sonni kiriting;"))
# print(fib(n))


#
# dic1={3:23,2:34,5:67,7:45}
# for i in dic1.keys():
#     print(f"keys ; {i}")
#
# sample={"class": {"student":{"name":"mike", "marks":{"physics":70,"history":80}}}}
# print(sample["class"]["student"]["marks"]["history"])
# #
# sample={"name":"kelly","age":112,"salary":5999,"city":"new york"}
# keys=['name','salary']
# dict1={}
# for i in keys:
#        dict1[i]=sample[i]
# print(dict1)
# #
# a=[3,3,4,5,6,6]
# b=[3,3,4,5,6,6]
#
# list1=dict (map(lambda x:(a[x],b[x]),))
# print(list1)
#
# a="salam1234"
# # list1={}
# # for i in a:
# #     list1[i]=a.count(i)
# # print(list1)
# list2={k:a.count(k) for k in a}
# print(list2)
#
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
# # def printpascal(qator):
#     maxw=len(' '.join(map(str, qator[-1])))
#     for list1 in qator:
#         list1str=' '.join(map(str,list1))
#         print(list1str.center(maxw))
# n=int(input("Pascal uchburchagi qatorini kiriting; "))
# pascaluchburchak=generatepascal(n)
# printpascal(pascaluchburchak)
#
#
# # def generatepascal(n):
# #     qator=[]
# #     for i in range(n):
# #         if i==0:
# #             qator.append([1])
# #         else:
# #             list1=[1]
# #             for j in range(1,i):
# #               list1.append(qator[i-1][j-1]+qator[i-1][j])
# #             list1.append(1)
# #             qator.append(list1)
# #     return qator
# # print(generatepascal(5))
# # def prints(qator):
# #     maxb=len(' '.join(map(str,qator[-1])))
# #     for list1 in qator:
# #         lst1str=' '.join(map(str,list1))
# #     print(lst1str.center(maxb))
# #
# # pascalj=generatepascal(5)
# # prints(pascalj)
#
#
#


