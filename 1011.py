#Nhập ma trận
A=[]
n = 2
m = 3
for i in range (0,n):
    Hang = []
    for j in range (0,m):
        print ("Nhập phân tử hàng ", i,"cột ", j, ": ")
        x = int(input())
        Hang.append(x)
    A.append(Hang)
    
#In ma trận
for i in range (0,n):
    for j in range (0,n):
        print (A[i][j], end = " ")
    print(A[i])

#Hàm nhập ma trận
def Nhapmatran_1 (A,n,m):
    for i in range (0,n):
        Hang = []
        for j in range (0,m):
            print ("Nhập phân tử hàng ", i,"cột ", j, ": ")
            x = int(input())
            Hang.append(x)
        A.append(Hang)

def Nhapmatran_2 (A,n,m):
    for i in range (0,n):
        A.append([])
        for j in range (0,m):
            print ("Nhập phân tử hàng ", i,"cột ", j, ": ")
            x = int(input())
            Hang.append(x)
        A.append(Hang)

#Hàm in ma trận
def Inmatran_1 (A,n,m):
    for i in range (0,n):
        for j in range (0,m):
            print(A[i][j],end=" ")
        print()

def Inmatran_2 (A,n):
    for i in range (0,n):
            print(A[i])

