#
# # 1-misol
# from faker import Faker
# import json
# from random import randint
#
# fake = Faker()
#
#
# def kiritishmalumot(x):
#     student_data = {}
#     for i in range(0, x):
#         student_data[i] = {}
#         student_data[i]['id'] = randint(1, 100)
#         student_data[i]['ism'] = fake.name()
#         student_data[i]['manzil'] = fake.address()
#         student_data[i]['yoshi'] = randint(1,76)
#         student_data[i]['manzili'] = str(fake.longitude())
#     print(student_data)
#
#     with open('students.json', 'w') as fp:
#         json.dump(student_data, fp)
#
#
# def main():
#     soni = 10
#     kiritishmalumot(soni)
#
#
# main()
#
#
import json

# Ma'lumotlar
foyda = {
    "ism": "John",
    "yosh": 30,
    "tillar": ["Inglizcha", "Fransuzcha"],
    "manzil": {
        "shahar": "New York",
        "indeks": "10001"
    },
    "o'quvchi": True
}

# JSON matnini faylga yozish
with open("foyda.json", "w") as fayl:
    json.dump(foyda, fayl)












