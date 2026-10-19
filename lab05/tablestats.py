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
    for r in rows:
        tip = row.get('тип')
        if tip:
            if tip not in count:
                count[tip] = 1
            else:
                count[tip]+=1
    return count
def total_minutes(rows,kind):
    itog = 0
    f = false
    for r in rows:
        if r.get('тип') == kind:
            f = True
            mi = row.get('минуты', '0')
            mi = mi.replace(',','.')
            trymi = mi.replace('-','',1).replace('.','',1)
            if trymi.isdigit():
                itog+=float(mi)
        if not(f):
            return 0
        return rount(itog,1)
            
