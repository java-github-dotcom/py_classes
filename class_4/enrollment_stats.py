universities = [
    ['California Institute of Technology', 2175, 37704],
    ['Harvard', 19627, 39849],
    ['Massachusetts Institute of Technology', 10566, 40732],
    ['Princeton', 7802, 37000],
    ['Rice', 5879, 35551],
    ['Stanford', 19535, 40569],
    ['Yale', 11701, 40500]
]

def enrollment_stats():
    ts = 0
    tt = 0
    for i in universities:
        ts=ts+i[1]
        tt=tt+i[2]
    print(f'Total students: {ts} \nTotal tuition: {tt}')
def mean():
    ms = 0 
    mt = 0
    for i in universities:
        ms=ms+i[1]
        mt=mt+i[2]
        ms = ms/len(universities)
        mt = mt/len(universities)
    print(f'Student mean: {ms} \nTuition mean: {mt}')
def median():
    ms = []
    mt = []
    for i in universities:
        ms.append(i[1])
        mt.append(i[2])
    ms = sorted(ms)
    ms = sorted(mt)
    ms = ms[int(len(universities)/2)]
    mt = mt[int(len(universities)/2)]
    print(f'Student median: {ms} \nTuition median: {mt}')

enrollment_stats()
mean()
median()







