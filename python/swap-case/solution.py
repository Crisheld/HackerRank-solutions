
def swap_case(s):
    result = ''    
    for c in s:
        result += c.lower() if c.isupper() else c.upper()

    return result

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)