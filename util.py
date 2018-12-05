def best(data, worst=False):
    index = best = 0
    best = data[index]
    for i in range(0, len(data)):
        if (worst and (data[i] < best)) or (not worst and data[i] > best):
            best = data[i]
            index = i
    return index, best
def get_data(day):
    return open('/home/dds/src/dds/advent18/%d/input.txt' % day)
