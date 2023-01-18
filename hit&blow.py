# coding:utf-8
import random

a = [random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9),
     random.randint(0,9)]

while True:
    isok = False
    while isok == False:
        b = input(" 数を入れてね＞ ")
        if len(b) != 4:
            print(" 4桁の数字を入力してください ")
        else:
            kazuok = True
            for i in range(4):
                if (b[i] < "0") or (b[i] > "9"):
                    print(" 数字ではありません ")
                    kazuok = False
                    break
            if kazuok:
                isok = True

    hit = 0
    for i in range(4):
        if a[i] == int(b[i]):
            hit = hit + 1

    blow = 0
    for j in range(4):
        for i in range(4):
            if(int(b[j]) == a[i]) and (a[i] != int(b[i])) and (a[j] != int(b[j])):
                blow = blow + 1
                break

    print(" ヒット " + str(hit))
    print(" ブロー " + str(blow))

    if hit == 4:
        print(" 当たり ")
        break

            
