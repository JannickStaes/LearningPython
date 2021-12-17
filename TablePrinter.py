#! python3
# prints a table of a list of string lists

tableDataExample = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]

def determineMaxColumnWidths(tableData):
    columnWidths =  [] #a list to store the max length of each string row, to be used as the max column width
    for stringList in tableData:
        maxLength = 0
        for word in stringList:
            if len(word) > maxLength:
                maxLength = len(word)
        columnWidths.append(maxLength)
    return columnWidths

def printTable(tableData):
    columnWidths = determineMaxColumnWidths(tableDataExample)
    rows = len(tableData[0]) #all lists are equal length so we can just take the first one
    columns = len(tableData)
    for row in range(rows):
        printRow = []
        for column in range(columns):
            printRow.append( tableData[column][row].rjust(columnWidths[column]))
        line = ' '.join( printRow )
        print(line)
 
printTable(tableDataExample)