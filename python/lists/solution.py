my_list = []


def exec_command(action, *args):
    if action == 'insert':
        my_list.insert(int(args[0]), int(args[1]))
    if action == 'print':
        print(my_list)
    if action == 'remove':
        my_list.remove(int(args[0]))
    if action == 'append':
        my_list.append(int(args[0]))
    if action == 'sort':
        my_list.sort()
    if action == 'pop':
        my_list.pop()
    if action == 'reverse':
        my_list.reverse()


if __name__ == '__main__':
    N = int(input())

    while N > 0:
        action, *args = input().split()
        exec_command(action, *args)
        N -= 1
