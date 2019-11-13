def spam():
    global eggs
    eggs = 'spam' #global

def bacon():
    eggs = 'bacon' #local

def ham():
    print(eggs) #global

def errorSpam():
    print(eggs)
    eggs = 'spam local'

eggs = 42
errorspam()
print(eggs)
