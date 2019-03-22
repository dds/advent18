from pprint import pprint
import util
import string
from collections import defaultdict
import string

sample_input = """
Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.
""".strip()

rawdata = util.get_data(7).read().split('\n')
# rawdata = sample_input.split('\n')

data = []

def parseLine(line):
    foo = line.split()
    prior, after = foo[1], foo[7]
    return (prior, after)

allSteps = set()
deps = defaultdict(list)
reverseDeps = defaultdict(list)

for i, line in enumerate(rawdata):
    if not line:
        continue
    prior, after = parseLine(line)
    data.append((prior, after))
    allSteps.add(prior)
    allSteps.add(after)
    deps[after].append(prior)
    reverseDeps[prior].append(after)

N = len(data)

remainingSteps = set(allSteps)
origDeps = dict(deps)

baseTime = 60
workers = 5
workerState = {
    # task: completion_time
    }

time = 0
stepOrder = []

while True:
    pprint('*' * 80)
    if not remainingSteps:
        break

    pprint('time: %s' % time)

    cS = []
    aW = []
    for worker in range(0, workers):
        if worker not in workerState:
            aW.append(worker)
        else:
            if time >= workerState[worker][1]:
                cS.append(workerState[worker][0])
                del workerState[worker]
                aW.append(worker)

    for step in cS:
        stepOrder.append(step)
        for d in reverseDeps[step]:
            deps[d].remove(step)
            pprint('deps[%s]=%s' % (d, deps[d]))
            if not len(deps[d]):
                del deps[d]

    tS = []
    aS = sorted(remainingSteps - set(deps.keys()))
    pprint('remainingSteps: %s' % remainingSteps)
    pprint('deps keys: %s' % deps.keys())
    if aS:
        steps = aS[:workers]
        taskTimes = [baseTime+string.uppercase.index(s)+1 for s in steps]
        pprint('steps: %s' % steps)
        pprint('taskTimes: %s' % taskTimes)
        for i, w in enumerate(aW[:len(steps)]):
            workerState[w] = (steps[i], time + taskTimes[i])
            tS.append(steps[i])

    pprint('workerState: %s' % workerState)
    for step in tS:
        remainingSteps.remove(step)
    time = min(ws[1] for ws in workerState.values())

pprint(''.join(stepOrder))
pprint('time: %s, workerState: %s' % (time, workerState))
