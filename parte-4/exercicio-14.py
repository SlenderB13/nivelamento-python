from datetime import date, datetime
import time

date = '2015, 50, 1' # 'year, number of week, weekday'
joel = datetime.strptime(date, '%Y, %W, %w')
print(time.asctime(joel.timetuple()))