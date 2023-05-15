
#8) Viết hàm đổi một số ở hệ thập phân sang hệ nhị phân
#(lưu dưới dạng chuỗi).
def chuyennhiphan(n):
    k = []
    while (n>0):
        a = int(float(n%2))
        k.append(a)
        n = (n-a)/2
    kq = ""
    k.reverse()
    for i in k:
        kq += str(i)
    return kq
n = int(input("Nhập số thập phân: "))
print("Số", n, "có dạng nhị phân là: ", chuyennhiphan(n))
