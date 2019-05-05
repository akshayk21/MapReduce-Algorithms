import MapReduce
import sys

"""
Implement a relational join as a MapReduce query

SELECT * 
FROM Orders, LineItem 
WHERE Order.order_id = LineItem.order_id

MapReduce query should produce the same result as this SQL query executed against an appropriate database.

You can consider the two input tables, Order and LineItem, as one big concatenated bag of records 
that will be processed by the map function record by record.
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    mr.emit_intermediate(record[1],record)

def reducer(key, list_of_values):
    list_of_items = []
    for value in list_of_values:
        if value[0] == 'order':
            order = value
        elif value[0] == 'line_item':
            list_of_items.append(value)
    
    for item in list_of_items:
        mr.emit(order + item)


# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
