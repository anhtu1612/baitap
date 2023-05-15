#1. Viết hàm Radian(d), tham số đầu vào là số thực là số đo góc theo độ bình thường.
#Hàm sẽ trả lại số đo của d theo radian. Công thức chuyển đổi: R=d*pi/180

n = float(input("Nhập số đo góc: "))
while n < 0 or n > 180:
    n = float(input("Nhập lại số đo góc: "))
def radian (d, pi=3.14):
    return (d*pi/180)
print("Số đo góc sau khi đổi là: ",radian(n))

#2. Viết hàm số f(m,n) với các tham số là các số tự nhiên. Hàm sẽ trả lại số nguyên lớn nhất
#đồng thời là ước chung của m và n. Nếu số đó không tồn tại thì trả về 0.

m = int(input("Nhập m: "))
n = int(input("Nhập n: "))
while m == 0 and n == 0:
    m = int(input("Nhập lại m: "))
    n = int(input("Nhập lại n: "))
def ucln (m,n):
    if (m == n):
        return ucln
    else:
        while (m != n):
            if m > n:
                m = m - n
            else:
                n = n - m
        if (m==1):
            return 0
        else:
            return m
print("Số nguyên lớn nhất đồng thời là ucln là: ",ucln(m,n))

#3. Viết hàm trả về số lượng các ký tự số có trong một số nguyên cho trước.
# Ví dụ Input: n=1234
#       Output: 4

n = int(input("Nhập số nguyên n: "))
while n <= 0:
    n = int(input("Nhập lại số nguyên n: "))
def skt(n):
    dem = 0
    while (n != 0):
        n = n//10
        dem += 1
    return dem
print("Số ký tự có trong số nuyên là: ",skt(n))
    
#4. Viết hàm trả về ước số chung lớn nhất của 2 số nguyên cho trước
    
a = int(input("Nhập số nguyên dương a = "))
b = int(input("Nhập số nguyên dương b = "))
def ucln(a,b):
    if (b == 0):
        return a
    return ucln(b, a%b)
print("Ước chung lớn nhất của", a, "và", b, "là", ucln(a,b))

