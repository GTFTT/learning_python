
# Alternative to switch case

def handle_value(val):
    match val:
        case 1: print('Here 1')
        case 2: print('Here 2')
        case 3 | 4 | 5:
            print('Here 3, 4, 5')
            print('No need for break')
        case _:
            print('Here default')

handle_value(1)
handle_value(2)
handle_value(4)
handle_value(5)
handle_value(10)