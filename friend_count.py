import MapReduce
import sys

"""
Consider a simple social network dataset consisting of a set of key-value pairs (person, friend) representing a 
friend relationship between two people. Describe a MapReduce algorithm to count the number of friends for each person.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    mr.emit_intermediate(record[0],record[1])

def reducer(key, list_of_values):
    mr.emit((key,len(list(set(list_of_values)))))


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
