## MapReduce-Algorithms

In this assignment, I have designed and implemented MapReduce algorithms for a variety of common data processing tasks. 

MapReduce.pyPreview the document that implements the MapReduce programming model. 
The framework faithfully implements the MapReduce programming model, but it executes entirely on a single machine -it does not involve parallel computation.

wordcount.py is the word count example implemented as a MapReduce program using the framework:

* In Part 1, we create a MapReduce object that is used to pass data between the map function and the reduce function.

* In Part 2, the mapper function tokenizes each document and emits a key-value pair. 
The key is a word formatted as a string and the value is the integer 1 to indicate an occurrence of word.

* In Part 3, the reducer function sums up the list of occurrence counts and emits a count for word. 
Since the mapper function emits the integer 1 for each word, each element in the list_of_values is the integer 1. The list of 
occurrence counts is summed and a (word, total) tuple is emitted where word is a string and total is an integer.

* In Part 4, the code loads the json file and executes the MapReduce query which prints the result to stdout.

### Problem 1: Creating and inverted index (inverted_index.py)
Create an Inverted index. Given a set of documents, an inverted index is a dictionary where each word is associated with 
a list of the document identifiers in which that word appears.

The .py file is run through the following command on the terminal:
$ python inverted_index.py books.json

### Problem 2: Implementing a relational join as a MapReduce query (join.py)
Consider the following query:

- SELECT * 
- FROM Orders, LineItem 
- WHERE Order.order_id = LineItem.order_id

The MapReduce query produces the same result as this SQL query executed against an appropriate database.

I have considered the two input tables, Order and LineItem, as one big concatenated bag of records that will
be processed by the map function record by record.

The .py file is run through the following command on the terminal:
$ python join.py records.json

### Problem 3: Counting the number of friends (friend_count.py)
In this part I have described a MapReduce algorithm to count the number of friends for each person.

Consider a simple social network dataset consisting of a set of key-value pairs (person, friend) representing 
a friend relationship between two people.

The .py file is run through the following command on the terminal:
$ python friend_count.py friends.json

### Problem 4: Non-symmetric friend relationships (asymmetric_friendships.py)
The relationship "friend" is often symmetric, meaning that if I am your friend, you are my friend. 
I have implemented a MapReduce algorithm to check whether this property holds. 
The scrips generates a list of all non-symmetric friend relationships

The .py file is run through the following command on the terminal:
$ python asymmetric_friendships.py friends.json

### Problem 5: Removing duplicates (unique_trims.py)

Consider a set of key-value pairs where each key is sequence id and each value is a string of nucleotides, 
e.g., GCTTCCGAAATGCTCGAA....

I have written a MapReduce query to remove the last 10 characters from each string of nucleotides, 
and then removing any duplicates generated. 

The .py file is run through the following command on the terminal:
$ python unique_trims.py dna.json

### Problem 6: Matrix multiplication (multiply.py)
Assumeing two matrices A and B in a sparse matrix format, where each record is of the form i, j, value, 
I have designed a MapReduce algorithm to compute the matrix multiplication A x B

The .py file is run through the following command on the terminal:
$ python multiply.py matrix.json
