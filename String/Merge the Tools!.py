def merge_the_tools(string, k):
    # your code goes here
    for i in range(0,len(string),k):
        a = string[i:i+k]
        s = []
        for l in a:
            if l not in s:
                s.append(l)
        print("".join(s))
       
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
