print('Введите заработную плату в месяц:')
salary = int(input())
print('Введите, какой процент(%) уходит на ипотеку')
mortgage = int(input())
print('Введите, какой процент(%) уходит на жизнь:')
life = int(input())
spent_on_mortgage_per_month = (mortgage * salary // 100)
spent_on_mortgage_per_year = spent_on_mortgage_per_month * 12
spent_per_life_per_month = (life * salary // 100)
spent_per_life_per_year = spent_on_mortgage_per_month * 12
accumulated_on_year = (salary - (spent_on_mortgage_per_month + spent_per_life_per_month))*12

print('На ипотеку было потрачено:', spent_on_mortgage_per_year)
print('Накоплено:', accumulated_on_year)
