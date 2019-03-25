import time

pattern = "%Y-%m-%d %H:%M"
month_pattern = '%m'

def get_normal_time():
    return time.strftime(pattern, time.localtime(time.time()))

def get_stamp_time(str_time):
    return int(time.mktime(time.strptime(str_time, pattern)))

def get_current_month():
    return int(time.strftime(month_pattern, time.localtime(time.time())))

def get_timestamp():
    return time.time()
if __name__ == '__main__':
    # str_time = '2019-03-20 17:36'
    # stamp_time = get_stamp_time(str_time)
    # print(stamp_time)
    get_current_month()