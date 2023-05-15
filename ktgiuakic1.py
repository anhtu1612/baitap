n = int(input("Nhập n: "))
dem = 0
for i in range (1, n+1):
    if i % 2 == 0:
        dem = dem + i
print("Tổng các số chẵn nằm trong đoạn [1,",n,"] là: ",dem)
