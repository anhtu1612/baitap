file = open("F:\code1.txt", "r")
L = file.readlines()
MT = []
for pt in L:
    li = pt.split()
    l=[int(x) for x in li]
    MT.append(l)
n = int(input("Nhập đỉnh: "))
if n - 1 >= 0 and n - 1 <= len(MT):
    print("Số đỉnh kề của đỉnh %s là: ", %(n))
    for i in range(0, len(MT[n-1])):
        if(MT[n-1][i]==1):
            print(i+1,end="")
