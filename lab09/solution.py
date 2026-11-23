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
    return c.tolist()
def cap_above(values, limit):
    a =  np.asarray(values)
    a[a>limit] = limit
    return a.tolist()
def celsius_to_fahrenheit(values):
    a =  np.asarray(values)
    fahrenheit = a * 9 / 5 + 32
    return fahrenheit.tolist()
