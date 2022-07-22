from datetime import datetime

string = 'Jan 1 2014 2:43PM'
date = datetime.strptime(string, '%b %m %Y %I:%M%p')
print(date)