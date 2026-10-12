def winner(names,scores):
    mx,mxi = 0,0
    for i in range(len(scores)):
        if scores[i]>mx:
            mx=scores[i]
            mxi=i
    return names[mxi]
def average(scores):
    if len(scores)>0:
        return round(sum(scores)/len(scores),2)
    else:
        return 0
def ranking(names,scores):
    ind = list(range(len(scores)))
    ind = sorted(ind, key = lambda i: scores[i],reverse=True)
    result = []
    for i in ind:
        result.append(names[i])
    return result
def above_average(names,scores):
    av = average(scores)
    result = []
    for i in range(len(names)):
        if scores[i]>av:
            result.append(names[i])
    return result
    
