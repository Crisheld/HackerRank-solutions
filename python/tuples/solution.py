if __name__ == '__main__':
    n = int(input())
    integer_list = list(map(int, input().split()))
    tuple_result = tuple(x for x in integer_list)
    print(hash(tuple_result))