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
def change_vector(values):
    c = np.asarray(values).copy()
    c[2:5] = 99
    c[::2] = -1
def cap_above(values, limit):
    a =  np.asarrau(values)
    a[a>limit] = limit
    return a.tolist()
def celsius_to_fahrenheit(values):
    a =  np.asarrau(values)
    fahrenheit = arr * 9 / 5 + 32
    return fahrenheit.tolist()
