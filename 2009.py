#1. Viết hàm trả về số nhỏ nhất của ba số nguyên cho trước.

def min(a,b,c):
    min = a
    if (min>b):
        min = b
    if (min>c):
        min = c
    return min
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
c = int(input("Nhập c: "))
print ("Vậy số nhỏ nhất trong 3 số là: ", min(a,b,c))

#2. Viết hàm kiểm tra một số có tổng các chữ số chia hết cho 3 hay không?
#Áp dụng hàm trên, viết chương trình tìm và in ra các số (<=1000) có tổng các chữ
#số chia hết cho 3.

def tong(n):
    temp = 0
    while (n!=0):
        temp = temp + n%10
        n = n/10
    return tong
    a = tong(n)
n = int(input("Nhập số n: "))
for n in range (1,10):
    if (a%3 == 0):
        print("Tổng các chữ số của số",n,"chia hết cho 3")
    else:
        print("Tổng các chữ số của số",n,"không chia hết cho 3")

#3. Viết hàm trả về số lượng chữ số có trong một số nguyên cho trước.
#    Ví dụ Input: 12345
#          Output: 5
#    Áp dụng hàm trên, viết chương trình nhập vào một số nguyên a, in ra màn hình
#số lượng chữ số có trong a.

def timso(n):
    dem = 0
    while (n != 0):
        n //= 10
        dem += 1
    return dem
n = int(input("Nhập số nguyên n: "))
if (n <= 0):
    n = int(input("Nhập lại n: "))
print("Số lượng chữ số có trong số nguyên",n,"là",timso(n))

def tongchuso(n):
    sum=0
    while n>0:
        n,so=divmod(n,10)
        sum=sum+so
    return sum
def tongsochiahet3(n):
    if tongchuso(n)%3==0:
        return true

#import math
#def pi(a):
 #   i=0
  #  m=0
   # while(abs((((-1)**i))/((2*i)+))>=a):
    #    m=m+(((-1))**i/((2*i)+1))
     #   i=i+1
    #return m*4*i
#a=float(input("Nhập a: "))
#print("Pi tinh được bằng: ",pi(a))
#print("Pi dã có bằng: ",math.pi)





























