#!/usr/bin/python
import re
import time
import datetime


dgname= 'NGFW-HOME'

months_linux = {'Jan':'01',
        'Feb':'02',
        'Mar':'03',
        'Apr':'04',
        'May':'05',
        'Jun':'06',
        'Jul':'07',
        'Aug':'08',
        'Sep':'09',
        'Oct':'10',
        'Nov':'11',
        'Dec':'12'
        }


months = {'January':'01',
        'February':'02',
        'March':'03',
        'April':'04',
        'May':'05',
        'June':'06',
        'July':'07',
        'August':'08',
        'September':'09',
        'October':'10',
        'November':'11',
        'December':'12'
        }



f = open('schedules.txt', 'r')
x = f.readlines()


all_strings = ''.join(x)

schedules = re.findall(r'time-range.*?!'  , all_strings,re.DOTALL)

#for s in schedules:
    #print(s)
    #print("++++++++++++++++++++++++++")

seconds = time.time()
human_time = time.ctime(seconds)


## Parsing the local time as a start date
l_month = human_time.split(' ')[1]
l_day = human_time.split(' ')[3]
if (int(l_day) < 10):
    l_day_zero = '0' + l_day
l_clock = human_time.split(' ')[4]
l_clock = l_clock[0:5]
l_year = human_time.split(' ') [5]


# iterating over every schedule and parsing the data
for s in schedules:
    s_name = s.split('\n')[0].split(' ')[1].strip()
    s_clock = s.split('\n')[1].split(' ')[3].strip()
    s_day = s.split('\n')[1].split(' ')[4].strip()
    s_month = s.split('\n')[1].split(' ')[5].strip()
    s_year = s.split('\n')[1].split(' ')[6].strip()
    #excluding expired schedules
    c_date = datetime.datetime(int(l_year), int(months_linux[l_month]), int(l_day))
    s_date = datetime.datetime(int(s_year), int(months[s_month]), int(s_day))
    if (c_date > s_date):
        continue 



    #print(s_name)
    #print(s_month)
    #print(s_day)
    #print(s_clock)
    #print(s_year)
    print("set device-group {} schedule {} schedule-type non-recurring {}/{}/{}@{}-{}/{}/{}@{}").format(dgname, s_name, l_year, months_linux[l_month], l_day_zero,l_clock,s_year, months[s_month], s_day, s_clock,)
