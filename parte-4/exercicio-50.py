from datetime import date, timedelta

start_date = date(2022, 7, 22)
end_date = date(2022, 5, 22)

dates = [(start_date + timedelta(x)).strftime('%Y-%m-%d') for x in range(1, int((start_date - end_date).days))]

for date in dates:
    print(date)