from datetime import datetime

date = datetime.today()
print(date.combine(date.date(), date.time().min))