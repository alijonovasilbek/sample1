'''
son topish o'yini
'''

# print("son topish o'yini o'ynaymiz")
# a=int(input(("0 dan 10 gacha son kiritnting; ")))
# count=0
import random
def sontop(x):
    tasodifiyson=random.randint(1,x)
    print(f"men 1 dan {x} gacha son o'yladim topa olaszmi?/")
    count=0
    while True:
       count+=1
       taxmin=int(input(">>>>>"))
       if taxmin<tasodifiyson:
           print("xato . men o'ylagan son bundan kattaroq")

       elif taxmin>tasodifiyson:
           print("men o'ylagan son bundan kichikroq")
       else:
           break
    print(f"tabriklaymiz {count} urinishda topdingiz")
    return count

def sonkom(x=10):
    input(f"1 dan {x} gacha son o'ylang va istalgan tugamani bosing")
    quyi=1
    yuqori=x
    taxminlar=0
    while True:
        taxminlar+=1
        if quyi!=0:
            taxmin=random.randint(quyi,yuqori)
        else:
            taxmin=quyi
        javob=input(f" siz  o'yldingiz: {taxmin}"
                    f"men o'ylagn son bundan katta +, yokki kichikk -".lower())

        if javob=="-":
            yuqori=taxmin-1
        elif javob=="+":
            quyi=taxmin+1
        else:
            break
    print(f" {taxminlar} urinishda topdm")
    return  taxmin

def play(x=10):
 yana=True
 while yana:

    user=sontop(x)
    komp=sonkom(x)


    if user < komp:
        print("tabriklaymiz siz yutdingiz:}")
    elif user > komp:
        print("men yutdm }")
    else:
        print(f"durrang hisob")
    yana=int(input("yana o'ynayszmi ha(1) yo(0)"))

play(10)









