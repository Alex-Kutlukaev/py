print('введите стороны треугольника')
a = int(input())
b = int(input())
c = int(input())
p = (a + b + c)/2
d = (p*(p-a)*(p-b)*(p-c)) **0.5
print(d)
