if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    result = sum(student_marks[query_name])
    result = result / len(student_marks[query_name])
    print(f"{result:.2f}")