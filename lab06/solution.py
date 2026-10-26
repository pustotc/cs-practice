def count_items(values):
    itog = {}
    for v in values:
        if v in itog:
            itog[v]+=1
        else:
            itog[v]=1
    return itog
def unique_sorted(values):
    return sorted(set(values))
def common(first, second):
    itog = []
    for f in first:
        if f in second:
            itog.append(f)
    return sorted(itog)
def only_in_first(first, second):
    itog = []
    for f in first:
        if f not in second:
            itog.append(f)
    return sorted(itog)
