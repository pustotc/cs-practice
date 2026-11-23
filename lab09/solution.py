import numpy as np
def make_hours():
    return np.arange(0,22,3).tolist()
def vector_report(values):
    d = {}
    d['third'] = values[2]
    d['last'] = values[-1]
    d['middle'] = values[2:6]
    d['every_second'] = values[::2]
    d['reversed'] = values[::-1]
    return d
print(vector_report(make_hours()))
