def codeWithComma(list):
    commalist = ''
    for i in range(len(list) - 2):
        commalist += list[i] + ', '
    commalist += list[-2] + ' and ' + list [-1]
    return commalist

list = ['pears', 'apples', 'bananas', 'tofu', 'cats']
commalist = codeWithComma(list) #list are passed by reference in Python so the function will modify the same list
print('This is the list, comma separated: \n')
print(commalist)