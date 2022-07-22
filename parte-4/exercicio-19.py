from datetime import datetime, timedelta

date = datetime.today()
print((date - timedelta(days=date.weekday() -1, weeks=1)).strftime('%Y-%m-%d'))