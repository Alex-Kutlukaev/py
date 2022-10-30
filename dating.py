boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
boys.sort()
girls.sort()
print('Идеальные пары:')
for boys,girls in zip(boys , girls):
    print(boys,'и',girls)
