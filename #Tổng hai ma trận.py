#Tổng hai ma trận
def Nhapmatran (A,n,m):
    for i in range (0,n):
        Hang = []
        for j in range (0,m):
            print ("Nhập phân tử hàng ", i,"cột ", j, ": ")
            x = int(input())
            Hang.append(x)
        A.append(Hang)
def Inmatran (A,n,m):
    for i in range (0,n):
        for j in range (0,m):
            print(A[i][j],end=" ")
        print()
def Tong2matran (A,B,n,m):
    C = []
    for i in range (0,n):
        C.append([])
        for j in range (0,m):
            C[i].append(A[i][j]+B[i][j])
    return C
Nhapmatran(A,n,m)
Nhapmatran(B,n,m)
C = Tong2matran(A,B,n,m)
print("Ma trận C: ")
Inmatran(C,n,m)


