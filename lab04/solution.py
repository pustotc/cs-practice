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
