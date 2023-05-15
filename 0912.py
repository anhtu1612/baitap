1
def nganhang(x):
    for i in range(0,3):
        tien = x*0.6/100*6
        x = x + tien
    print("Số tiền sau 18 tháng là: ", x)

x = int(input("Nhập số tiền gửi ngân hàng: "))
nganhang(x)

