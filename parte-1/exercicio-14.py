from datetime import date

initial_date = date(2024, 9, 2)
final_date = date(2022, 7, 18)

days = (initial_date - final_date).days
print(f'Days: {days}')