import util
from datetime import datetime
from collections import defaultdict
from pprint import pprint
import re

sample_input = """\
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up"""

def parseLine(line):
    # [1518-11-05 00:03] Guard #99 begins shift
    # [YYYY-MM-DD hh:mm] {"Guard #ID begins shift"; "wakes up"; "falls asleep"}
    if line[0] != '[':
      next
    year = int(line[1:5])
    month = int(line[6:8])
    day = int(line[9:11])
    hour = int(line[12:14])
    minute = int(line[15:17])
    event = line[19:]
    return (datetime(year, month, day, hour, minute), event)

sleepTimes = defaultdict(list)
guardId = None
sleeping = False
lastEventTime = None
eventLog = []
for line in util.get_data(4):
    timestamp, event = parseLine(line)
    eventLog.append((timestamp, event))

eventLog = sorted(eventLog, key=lambda x: x[0])
for (timestamp, event) in eventLog:
    if event.startswith('Guard'):
        guardId = int(re.findall('\d+', event[7:])[0])
    if event.startswith('falls asleep'):
        sleeping = True
        lastEventTime = timestamp
    if event.startswith('wakes up'):
        sleeping = False
        sleepTimes[guardId].append((lastEventTime, timestamp))

maxSleep = 0
sleepiestGuard = 0
for guard in sleepTimes:
    sleep = 0
    for start, end in sleepTimes[guard]:
        sleep += (end - start).seconds / 60
    if sleep > maxSleep:
      maxSleep = sleep
      sleepiestGuard = guard

mostDaysSlept = 0
bestMinute = 0
for minute in xrange(0, 59):
  daysSlept = 0
  for start, end in sleepTimes[sleepiestGuard]:
      if start.minute <= minute < end.minute:
          daysSlept += 1
  if daysSlept > mostDaysSlept:
      mostDaysSlept = daysSlept
      bestMinute = minute
print 'A: %d' % (sleepiestGuard * bestMinute)

guardMinutes = defaultdict(dict)
mostSleepingDays = 0
bestMinute = 0
mostFrequentlySleeping = 0
for minute in xrange(0, 59):
    for guard in sleepTimes:
        daysSleeping = 0
        for start, end in sleepTimes[guard]:
            if start.minute <= minute < end.minute:
                guardMinutes[minute][guard] = guardMinutes[minute].get(guard, 0) + 1
                if guardMinutes[minute][guard] > mostSleepingDays:
                    mostFrequentlySleeping = guard
                    mostSleepingDays = guardMinutes[minute][guard]
                    bestMinute = minute

print 'B: %d' % (bestMinute * mostFrequentlySleeping)
