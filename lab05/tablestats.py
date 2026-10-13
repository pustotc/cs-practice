def read_rows(lines):
    zag = None
    allline = []
    for line in lines:
        line = line.strip('\n')
        if not line.strip():
            continue
        linel = [x.strip() for x in line.split(',')]
        if zag is None:
            zag = linel
            continue
        if len(linel) != len(zag):
            continue
        lined = {}
        for z,l in zip(zag,linel):
            lined[z]=l
        allline.append(lined)
    return allline
def count_types(rows):
    count = {}
    if not rows:
        return count
    fk = list(rows[0].keys())[0]
    for r in rows:
        tip = row.get(fk)
        if tip:
            if tip not in count:
                count[tip] = 1
            else:
                count[tip]+=1
    return count
