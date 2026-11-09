def reshape_rows(values, width):
    if len(values) % width != 0:
        return []
    result = np.array(values)
    return result.reshape(-1,width)
def block(matrix, rows, columns):
    result = np.array(matrix)
    result = result[np.ix_(rows,columns)]
    return result
def column_means(matrix):
    result = np.array(matrix)
    result = np.mean(result,axis=0)
    return result
def column_range(matrix, column):
    
    
    
    
