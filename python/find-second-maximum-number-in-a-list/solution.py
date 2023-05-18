if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

    runner_up = -100
    max = arr[0]

    for i in arr:
        if i > max:
            runner_up = max
            max = i
        elif i > runner_up and i < max:
            runner_up = i

    print(runner_up)
