if __name__ == '__main__':
    python_students = []
    lowest_score = float('inf')
    second_lowest_score = float('inf')
    
    for _ in range(int(input())):
        name = input()
        score = float(input())
        python_students.append([name, score])
        if score < lowest_score:
            second_lowest_score = lowest_score
            lowest_score = score
        elif score < second_lowest_score and score > lowest_score:
            second_lowest_score = score
        
    
    filtered = list(filter(lambda s: s[1] == second_lowest_score, python_students))
    filtered.sort(key=lambda s: s[0])
    for s in filtered:
        print(s[0])
