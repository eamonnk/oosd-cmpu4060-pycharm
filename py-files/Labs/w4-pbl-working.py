>>> print("{: <10}".format("TEST"))
TEST~~~~~~
>>> print("{: >10}".format("TEST"))
~~~~~~TEST
>>> print("{:~^10}".format("TEST"))
~~~TEST~~~
>>> print("{:~=10}".format(-10))
>>> print("{:~^10}".format("TEST"))
~~~TEST~~~
'''
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Indexing using a for loop
rows = len(matrix)
columns = len(matrix[0])

print(&quot;\nUsing For Loop:&quot;)
for i in range(rows):
    for j in range(columns):
        print(f&quot;Element at ({i}, {j}): {matrix[i][j]}&quot;)

flat_list = [element for row in matrix for element in row]
print(flat_list)
print(&quot;\nUsing List Comprehension:&quot;)
print(&quot;Flattened List:&quot;, flat_list)
    '''