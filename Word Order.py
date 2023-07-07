# Enter your code here. Read input from STDIN. Print output to STDOUT
a = int(input())
lst = []
wrdlst = []
count = ''
dct = {}
for i in range(a):
    word = input()
    if word not in dct.keys():
        dct.update({word:1})
    else:
        dct[word] = dct[word] + 1
print(len(dct))
for i in dct:
    print(dct[i],end = ' ')

