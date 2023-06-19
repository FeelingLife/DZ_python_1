# Задача 6: Счастливый билет, сумма трех первых чисел равна сумме трех последних чисел

bilet = int(input("Введите шестизначный номер билета: "))
print(bilet)
s1 = int((bilet/100000))
s2 = int((bilet/10000%10))
s3 = int((bilet/1000%100%10))
s123 = s1 + s2 + s3

s4 = int((bilet%1000/100))
s5 = int((bilet%100/10))
s6 = int((bilet%10))
s456 = s4 + s5 + s6

if (s123==s456):
   print("YES!")
else: print("NO!")