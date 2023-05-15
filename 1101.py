#1) Đếm số ký tự chữ số có trong một chuỗi cho trước.
dem = 0
s = str(input('Nhập chuỗi: '))
for i in s:
    if i.isdigit():
        dem = dem + 1
print('Số lượng ký tự số có trong %s là: %d' %(s,dem))

#2) Đếm số ký tự là chữ cái (chữ hoa hoặc chữ thường)
#có trong một chuỗi cho trước.
s=input("Nhập chuỗi: ")
dem=0
for x in s:
    if x.isalpha():
        dem=dem+1
print("Số lượng ký tự có trong %s là %d" %(s,dem))

#3) Viết hàm Tachten(Hoten):
#Tách tên của chuỗi Hoten cho trước.
s = str(input('Nhập Họ tên: '))
L = s.split()
print(L)
print("Họ: ", L[0]);
print("Tên:", L[-1]);
print("Ten 2:", L[len(L)-1]);

print("Ho dem:", L[1:len(L)-1]);
Hodem=''
for i in range (1,len(L)-1):
    Hodem = Hodem + L[i] +' '
print(Hodem.rstrip())

#4) Viết hàm Tachho(Hoten):
#Tách họ của chuỗi Hoten cho trước.
s = input("Nhập họ tên")
L = s.split()
print (L[0])

#5) Viết chương trình nhập vào họ và tên của một người, in ra họ, chữ đệm
#và tên của người đó.
def ten(s):
    L = s.split()
    print(L)
    print("Họ: ", L[0]);
    hodem=' '
    for i in range (1,len(L)-1):
        hodem = hodem + L[i] +' '
    print("Họ đệm:", hodem.rstrip())
    print("Tên:", L[-1]);
s = str(input('Nhập Họ tên: '))
print(ten(s))

#6) Viết hàm xóa các ký tự trắng thừa
#giữa trong một chuỗi cho trước.
def xoakhoangtrang(s):
    s=" ".join(s.split())
    return s
s=str(input("Nhập chuỗi: "))
print("Chuỗi sau khi xoá khoảng trắng là: ",xoakhoangtrang(s))

#7) Viết hàm đảo một chuỗi cho trước
def daochuoi(s):
    L = list(reversed(s))
    L_new = ''.join(L)
    return L_new
s=str(input("Nhập chuỗi: "))
print("Chuỗi sau khi đảo là: ",daochuoi(s))

#8) Viết hàm đổi một số ở hệ thập phân sang hệ nhị phân
#(lưu dưới dạng chuỗi).

    
