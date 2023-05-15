n = int(input("Nhập số phần tử: "))
A = list(map(int,input().split()))
x = int(input("Nhập số: "))
dem = 0
def chiahet(n):
    for i in range (0,n):
        if A[i] % x == 0:
            dem = dem + 1
    return dem
print(min(A))
print(sorted(A,reverse = True))
