#

A=[]
n = int(input("Nhập số phần tử: "))
for i in range(0,n):
    x = int(input("Nhập số: "))
    A.append(x) #A=A+(x)
for x in A:
    print(A[i],end=" ")

#1

def nhapmang(A,n):
    for i in range(0,n):
        x=int(input("Nhập số: "))
        A.append(x)
def inmang(A,n):
    for i in range (0,n):
        print(A[i], end= " ")

A=[]
n = int(input("Nhập số phần tử: "))
nhapmang(A,n)
inmang(A,n)
x = int(input("Nhập vào một số nguyên: "))
print("Số phần tử có giá trị bằng",x,"là: ",A.count(x))
    
#2

def chuyennhiphan(n):
    L=[]
    while n!=0:
        sodu=n%2
        L.append(sodu)
        n=n//2
    L.revese()
    return L
n=int(input("Nhập số n: "))
print("Số hệ 2 cần tìm: ")
L=chuyennhiphan(n)
for x in L:
    print(x, end=" ")

