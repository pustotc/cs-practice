def winner(scores):
    mx,mxi = 0,0
    for i in range len(scores):
        if scores[i]>mx:
            mx=scores[i]
            mxi=i
    return mxi
def average(scores):
    if len(scores)>0:
        return sum(scores)/len(scores)
def ranking(scores,names):
    ind = list(range(len(scores)))
    ind = sorted(ind, key = lambda i: scores[i])
    ind.reverse
    result = []
    for i in ind:
        result.append(names[i])
    return result
def above_average(scores,names):
    av = average(scores)
    result = []
    for i in range(len(names)):
        if scores[i]>av:
            result.append(names[i])
    return result
    
