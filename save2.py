import os
# a = open("text2.txt","w")
# print(1,file=a)
# a.close()
#  a = open("text2.txt","r")
#  q=a.read()
#
# if a == 1:
#     schet = 1
#
#
#
#
#     if schet == 1:
#         print("начинаем счёт с начала,номер " + str(schet))
#         a = open("text2.txt", "w")
#         schet += 1
#         print(schet, file=a)
#         a.close()
#
# if  int(q) > 1:
#     a.close()
#     a = open("text2.txt", "r")
#     schet = a.read()
#     schet = int(schet)
#     print("продолжаем счёт,номер " + str(schet))
#     schet += 1
#     a.close()
#     a = open("text2.txt", "w")
#     print(schet, file=a)
#     a.close()

# if schet < 1:
#     print("agrizyak")

# a = open("text2.txt","w")
# print(schet,file=a)
# a.close()
# a = open("text2.txt","r")
# q=a.read()
# a.close()


# если нету файла то
#     открыть файл(создать)
#     написать цифру
#     закрыть файл
#     написать эту цифру в консоль
#
# если файл есть то
#     открыть файл
#     прочитать из него число
#     написать это число+1 в консоль
#     закрыть файл
#     открыть файл
#     записать число из консоли в файл
#     закрыть файл

if os.path.exists("text2.txt"):
    a = open("text2.txt","r")
    q = a.read()
    q=int(q)
    d=q+1
    print("продолжаем счёт,номер "+ str(d))
    a.close()
    a = open("text2.txt","w")
    print(d,file=a)
    a.close()
else:
    a = open("text2.txt","w")
    print(1,file=a)
    a.close()
    print("начинаем счёт,номер 1")









