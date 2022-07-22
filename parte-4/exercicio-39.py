from datetime import date

birth = date(2000, 2, 18)
age = abs(birth - date.today()).days
print(date.fromordinal(age - 365).year)