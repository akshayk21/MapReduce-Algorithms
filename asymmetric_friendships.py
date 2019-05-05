import MapReduce
import sys

"""
The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. 
Implement a MapReduce algorithm to check whether this property holds. 
Generate a list of all non-symmetric friend relationships.

"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    pair = [record[0], record[1]]
    pair.sort()
    mr.emit_intermediate((pair[0],pair[1]),1)

def reducer(key, list_of_values):
    if len(list_of_values)<2:
        mr.emit(key)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
