A = int(input())
B = int(input())
H = int(input())
if A >= H:
    print('Недосып')
elif H >= B:
    print('Пересып')
elif H >= A:
    print('Это нормально')