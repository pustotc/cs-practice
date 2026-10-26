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
