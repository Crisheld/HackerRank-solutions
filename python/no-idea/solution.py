
if __name__ == '__main__':
    # n, m = input().split()
    # integer_list = map(int, input().split())
    # set_a = map(int, input().split())
    # set_b = map(int, input().split())

    f = open('python/no-idea/test_case_8.txt')

    n, m = f.readline().split()
    integer_list = list(map(int, f.readline().split()))
    set_a = list(map(int, f.readline().split()))
    set_b = list(map(int, f.readline().split()))

    f.close()

    happiness = 0


    index_set_a = {num: i for i, num in enumerate(set_a)}
    index_set_b = {num: i for i, num in enumerate(set_b)}

    for i in integer_list:
        if i in index_set_a:
            happiness += 1
        if i in index_set_b:
            happiness -= 1

    print(happiness)

