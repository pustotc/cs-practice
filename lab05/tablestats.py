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
