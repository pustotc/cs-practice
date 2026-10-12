def winner(scores):
    mx,mxi = 0,0
    for i in range len(scores):
        if scores[i]>mx:
            mx=scores[i]
            mxi=i
    return mxi
