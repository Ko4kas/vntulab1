n = int(input("На скільки років батько старший: "))
m = int(input("У скільки разів батько старший: "))
son = n // (m - 1)
father = son * m
print(f"Вік батька: {father}, вік сина: {son}")