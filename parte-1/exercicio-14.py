from datetime import date

initial_date = date(2022, 9, 2)
final_date = date(2024, 7, 18)

days = abs((initial_date - final_date).days)
print(f'Days: {days}')
#TODO: DEIXAR O ABS NA VARIAVEL