def swap_case(s):
    u = ""
    for l in s:
        if l.islower():
            u = u + l.upper();
        else:
            u = u + l.lower()
    return u

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
