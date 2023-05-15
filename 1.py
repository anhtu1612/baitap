#1. Tính tổng các số tự nhiên lẻ nhỏ hơn n
    tong = 0
    n = int(input("Nhập n:"))
    while (n<=0):
        n = int(input("Nhập lại n: "))
    if (n>0):
        for i in range(0, n+1):
            if i%2 != 0:
                tong += i
        print ("Tổng các số tự nhiên lẻ nhỏ hơn", n, "là: ", tong)
                
#2. In ra các số nguyên tố trong đoạn [a,b] cho trước
import math
    a = int(input("Nhập a: "))
    b = int(input("Nhập b: "))
    while (a<=b and a<2):
        a = int(input("Nhập lại a: "))
    for i in range(a, b+1):
        if i>1:
            for j in range(2, int(math.sqrt(i))+1):
                if i%j == 0:
                    break
            else:
                print ("Các số nguyên tố trong đoạn [",a,",",b,"] là: ",i)
                
#3. Viết đoạn chương trình kiểm tra tính hợp lệ của ngày nhập vào (day, month, year)
    ngay,thang,nam = (int(input("Nhập Ngày, Tháng, Năm: ")
        def case1(
