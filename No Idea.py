# Enter your code here. Read input from STDIN. Print output to STDOUT
a = input().split()
b = input().split()
c = set(input().split())
d = set(input().split())
sum = 0
for x in b:
    if x in c:
        sum = sum + 1
    if x in d:
        sum = sum - 1
print(sum)
