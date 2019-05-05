import MapReduce
import sys

"""
Assume you have two matrices A and B in a sparse matrix format, 
where each record is of the form i, j, value. 
Design a MapReduce algorithm to compute the matrix multiplication A x B

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

K = 5
def mapper(record):
	#K=5
    matrix, row, col, val = record
    if matrix == 'a':
        for n in range(K):
            mr.emit_intermediate((record[1], n), [matrix, col, val])
    else:
        for n in range(K):
            mr.emit_intermediate((n, record[2]), [matrix, row, val])

def reducer(key, list_of_values):
    result_A, result_B = [],[]
    for val in list_of_values:
        if val[0]=='a':
            result_A.append(val)
        else:
            result_B.append(val)
    
    result = 0
    
    for a in result_A:
        for b in result_B:
            if a[1] == b[1]:
                result += a[2] * b[2]
    
    mr.emit((key[0], key[1], result))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
