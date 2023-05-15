def snt(n):
    dem = 1;
    if (n <2):
        dem = 0
        return flag  
    for i in range(2, n):
        if n % i == 0:
            dem = 0
            break
    return dem
n = int(input("Nhập n: "))
if snt(n) == 1:
    print(n," là số nguyên tố")
else:
    print(n," không phải là số nguyên tố")
