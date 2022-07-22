from datetime import datetime, timedelta

current_date = datetime.today().date() - timedelta(5)

print(f'Current date: {datetime.today().date()}')
print(f'5 days before current date: {current_date}')