#фУНКЦИя ZIP

#=====================================================================================#

#1)

#ОБЫЧНАЯ ФУНКЦИЯ
a = [5, 6, 7, 8]

b = [100, 200, 300, 400]

for i in range(4):
    print(a[i], b[i])

#ОТВЕТ:
# 5 100
# 6 200
# 7 300
# 8 400





#ФУНКЦИЯ ZIP
a = [5, 6, 7, 8]

b = [100, 200, 300, 400]

rez = zip(a, b)
print(list(rez))

#ОТВЕТ: [(5, 100), (6, 200), (7, 300), (8, 400)]


#ИЛИ ЖЕ ТАК
a = [5, 6, 7, 8]

b = [100, 200, 300, 400]

rez = list(zip(a, b))
print(rez)

#ОТВЕТ: [(5, 100), (6, 200), (7, 300), (8, 400)]






#А ТАК-ЖЕ МОЖЕМ И ТАК:
a = [5, 6, 7, 8]

b = [100, 200, 300, 400]

c = 'abcd'

rez = list(zip(a, b, c))
print(rez)

#ОТВЕТ: [(5, 100, 'a'), (6, 200, 'b'), (7, 300, 'c'), (8, 400, 'd')]






#А ТАК-ЖЕ МОЖЕМ И ТАК:

a = [5, 6, 7, 8]

b = [100, 200, 300, 400]

c = 'abcd'

for t1,t2,t3 in zip(a,b,c):
 print(t1,t2,t3)

#ОТВЕТ: 
# 5 100 a
# 6 200 b
# 7 300 c
# 8 400 d





#ТЕПЕРЬ КАК ВЕРНУТЬ ВСЕ ОБРАТНО
a = [5, 6, 7, 8]

b = [100, 200, 300, 400]

c = 'abcd'

rez = (zip(a, b, c))

col1,col2,col3 = zip(*rez)
print(col1,col2,col3)

#ОТВЕТ: (5, 6, 7, 8) (100, 200, 300, 400) ('a', 'b', 'c', 'd')