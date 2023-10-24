katz_deli = []

def line(queue):
    if len(queue) == 0:
        print("The line is currently empty.")
    else:
        new_line = [f'{queue.index(person) + 1}. {person}' for person in queue ]
        print(f'The line is currently: {" ".join(new_line)}')

line(katz_deli)

def take_a_number(queue, new_cust):
    queue.append(new_cust)
    print(f'Welcome, {new_cust}. You are number {queue.index(new_cust) + 1} in line.')

def now_serving(queue):
    if len(queue) > 0:
        print(f'Currently serving {queue[0]}.')
        queue.pop(0)
    else:
        print('There is nobody waiting to be served!')