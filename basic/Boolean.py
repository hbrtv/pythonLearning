# Three aspects about Boolean type
# Boolean Value, Boolean Operator, Boolean expression(condition)
# Boolean Value can only be True or False With Captical Character in the first place

while True:
    problem = input("problem type: ")
    if problem == 'befuddled':
        __import__('pprint').pprint('problem has not been solved')
        __import__('pprint').pprint('you shouldn\'t lost your temper')
        __import__('pprint').pprint('prety print')
    elif problem == 'solved':
        __import__('pprint').pprint('Congratulation!')
        print('you should be proud of yourself')
    elif problem == 'exit':
        break
    elif problem == 'cloud' or problem == 'yun':
        __import__('pprint').pprint('*******')
        print('befuddled')
        __import__('pprint').pprint('*******')
    else:
        print('Shoudinger\'s problem')
        # This is what happen when while block come to end
        # It will continue to the star of the loop
        continue

for i in range(0,5,1):
    print('debate')
    print('silent')
    print('sad')
    print('metting')
    print('talking')
    print('joyful')
    print('fear')
    continue
    print('courage')
    print('in relationship')
