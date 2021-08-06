import schedule
import time
import datetime
# schedule

def my_func():
    print('salom')

schedule.every(1).seconds.do(my_func)

while True:
    if datetime.datetime.now().strftime('%H,%M') == '15,13':
        schedule.run_pending()
    else:
        break

# while schedule:
#     schedule.run_pending()
#     time.sleep(1)

