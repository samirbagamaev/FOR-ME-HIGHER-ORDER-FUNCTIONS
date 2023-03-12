#ФУНКЦИЯ ENUMERATE

#=====================================================================================#

#1)

a = [10, 20, 30, 40]

print(list(enumerate(a)))

#ОТВЕТ: [(0, 10), (1, 20), (2, 30), (3, 40)]

#ФУНКЦИЯ ENUMERATE ДОБАВЛЯЕТ ПОРЯДКОВОЕ ЧИСЛО НАЧИНАЯ С 0 (ИНДЕКС)




#2)

a = [10, 20, 30, 40]

for para in enumerate(a):
    print(para)

#ОТВЕТ:
# (0, 10)
# (1, 20)
# (2, 30)
# (3, 40)






#ИЛИ ЖЕ ТАК
a = [10, 20, 30, 40]

for index,value in enumerate(a):
    print(index,value)

#ОТВЕТ:
# 0 10
# 1 20
# 2 30
# 3 40






#3)
#ВЫВЕДЕМ ТОЛЬКО ТЕ ЗНАЧЕНИЯ,КОТОРЫЕ ДЕЛЯТСЯ НА 20

a = [10, 20, 30, 40]

for index,value in enumerate(a):
    if value % 20 == 0:
     print(index,value)

#ОТВЕТ:
# 1 20
# 3 40




#4)

a = [10, 20, 30, 40]
s = 'hello'

for index,value in enumerate(s):
 print(index,value)

#ОТВЕТ:
# 0 h
# 1 e
# 2 l
# 3 l
# 4 o





#5)
#ИЛИ ЖЕ ТАК

a = [10, 20, 30, 40]
s = 'hello'
t = ('banana', 'apple', 'mango')

for index,value in enumerate(t):
 print(index,value)

#ОТВЕТ:
# 0 banana
# 1 apple
# 2 mango






#6)
#ИЛИ ЖЕ ТАК

a = [10, 20, 30, 40]
s = 'hello'
t = ('banana', 'apple', 'mango') #кортеж
d = {'a':1, 'b':2, 'c':3}

for index,value in enumerate(d):
 print(index,value)

#ОТВЕТ:
# 0 a
# 1 b
# 2 c





#7)
#ИЛИ ЖЕ ТАК

a = [10, 20, 30, 40]
s = 'hello'
t = ('banana', 'apple', 'mango') #кортеж
d = {'a':1, 'b':2, 'c':3}

for index,value in enumerate(range(10,20)):
 print(index,value)

#ОТВЕТ:
# 0 10
# 1 11
# 2 12
# 3 13
# 4 14
# 5 15
# 6 16
# 7 17
# 8 18
# 9 19





#8)
#ТАК-ЖЕ МОЖНО ИЗМЕНИТЬ ПОРЯДКОВЫЙ НОМЕР

a = [10, 20, 30, 40]
s = 'hello'
t = ('banana', 'apple', 'mango') #кортеж
d = {'a':1, 'b':2, 'c':3}

for index,value in enumerate(a,100):
 print(index,value)

#ОТВЕТ:
# 10 banana
# 11 apple
# 12 mango






#9)
#ИЛИ ЖЕ ВОТ ТАК
#ТАК-ЖЕ МОЖНО ИЗМЕНИТЬ ПОРЯДКОВЫЙ НОМЕР

a = [10, 20, 30, 40]
s = 'hello'
t = ('banana', 'apple', 'mango') #кортеж
d = {'a':1, 'b':2, 'c':3}

for index,value in enumerate(a,100):
 print(index,value)

#ОТВЕТ:
# 100 10
# 101 20
# 102 30
# 103 40