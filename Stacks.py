

top = None
stack = [None for i in range(6)]


def init_stack():
    for i in range(5):
        stack[i] = None


def push(pushed_data):
    global top, stack
    if top == 5:
        print("stack overflow, please pop data before pushing.")
    else:
        top += 1
        stack[top] = pushed_data


def pop():
    global top, stack
    if top is None:
        print("stack underflow, please push data before popping")
    else:
        top -= 1
        stack[top] = None


def display_stack():
    for i in range(5, 0, -1):
        print(stack[i])


init_stack()
push()
display_stack()


