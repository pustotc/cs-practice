names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]
def winner(names,scores):
    mx,mxi = min(scores),0
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
if __name__ == '__main__':
    print(winner(names, scores))
    print(average(scores))
    print(ranking(names, scores))
    print(above_average(names, scores))
