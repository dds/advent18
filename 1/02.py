import sys

frequency_list = []
for line in sys.stdin:
    try:
        frequency_list.append(int(line))
    except:
        print "Could not parse: %s" % line
        raise

index = 0
frequency = 0
frequency_history = {}
looped = 0

while True:
  frequency += frequency_list[index]
  if frequency not in frequency_history:
      frequency_history[frequency] = 1
  else:
      break
  index = (index + 1) % len(frequency_list)
  if index == 0:
      looped += 1

print "frequency %d found at index %d (looped %d)" % (frequency, index, looped)
