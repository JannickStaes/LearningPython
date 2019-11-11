print('What is your name?') #ask for their name
my_name = input()
print('And your age?')
my_age = input()

if my_name == 'Alice':
    print('Hi, Alice!')
elif int(my_age) < 12:
    print('You are not Alice, kiddo.')
elif my_age > 2000:
    print('Unlike you, Alice is not an undead, immortal vampire.')
elif my_age > 100:
    print('You are not Alice, grannie.')