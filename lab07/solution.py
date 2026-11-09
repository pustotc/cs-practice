def reshape_rows(values, width):
    if len(values) % width != 0:
        return []
    result = np.asarray(values)
    return np.rount(result.reshape(-1,width),6).tolist()
def block(matrix, rows, columns):
    if not matrix:
        return []
    result = np.asarray(matrix)
    result = result[np.ix_(rows,columns)]
    return np.round(result,6).tolist()
def column_means(matrix):
    if not matrix or len(matrix)==0:
        return []
    result = np.asarray(matrix)
    result = np.mean(result,axis=0)
    return np.round(result,6).tolist()
def column_range(matrix, column):
    if not matrix or len(matrix)==0:
        return 0.0
    m = np.asarray(matrix)
    mColumn = m[:,column]
    return float(np.round(np.max(mColumn) - np.min(mColumn),6))
    
    
    
    
