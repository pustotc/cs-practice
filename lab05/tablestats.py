def read_rows(lines):
    zag = None
    allline = []
    for line in lines:
        cleaned = line.strip('\n')
        if not cleaned.strip():
            continue
        linel = [x.strip() for x in cleaned.split(',')]
        if zag is None:
            zag = linel
            continue
        if len(linel) != len(zag):
            continue
        lined = {}
        for z, l in zip(zag, linel):
            lined[z] = l
        allline.append(lined)
    return allline
def count_types(rows):
    count = {}
    for r in rows:
        tip = r.get('тип')
        if tip:
            if tip not in count:
                count[tip] = 1
            else:
                count[tip] += 1
    return count
def total_minutes(rows, kind):

    itog = 0.0
    for r in rows:
        if r.get('тип') == kind:
            mi = r.get('минуты', '0')
            if mi:
                mi = mi.replace(',', '.')
                try:
                    itog += float(mi)
                except ValueError:
                    continue
    return round(itog, 1)
def to_csv(counts):
    lines = ['тип,количество']
    for kind in sorted(counts.keys()):
        lines.append(f"{kind},{counts[kind]}")
    return '\n'.join(lines) + '\n'
