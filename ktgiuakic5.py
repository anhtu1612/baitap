def xulichuoi(s):
    s1 = s.split()
    lst = ''
    for i in s1:
        if len(i) > len(lst):
            lst = i
    return lst
n=1
while n:
    s = input()
    a = s.split()
    print(len(xulichuoi(s)))
    print(len(a))
    n = n - 1
