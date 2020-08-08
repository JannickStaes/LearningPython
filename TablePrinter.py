#! python3
# prints a table of a list of string lists

tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

for stringList in tableData:
    for word in stringList:
        print(word + ' \n')

