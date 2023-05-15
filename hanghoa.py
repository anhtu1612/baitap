
class HANGHOA:
    def __init__(self,mahang,tenhang,soluong,giaban):
        self.mahang = mahang
        self.tenhang = tenhang
        self.soluong = soluong
        self.giaban = giaban
    def nhap(self):
        self.mahang = input("Nhập mã hàng: ")
        self.tenhang = input("Nhập tên hàng: ")
        self.soluong = int(input("Nhập số lượng: "))
        self.giaban = int(input("Nhập giá bán: "))
    def xuat(self):
        print("Mã hàng: ",self.mahang)
        print("Tên hàng: ",self.tenhang)
        print("Số lượng: ",self.soluong)
        print("Giá bán: ",self.giaban)
    def __str__(self):
        return "Mã hàng: {}\nTên hàng: {}\nSố lượng: {}\nGiá bán: {}".format(self.mahang, self.tenhang, self.soluong, self.giaban)
def check(DS,ma,k):
    for i in range(k):
        if DS[i].mahang == ma:
            return False
    return True
while True:
    n = int(input("Nhập số hàng hoá: "))
    if n <= 100:
        break
DS=[]
for i in range(n):
    while True:
        mahang = input("Nhập mã hàng: ")
        if check(DS,mahang,i):
            break
    tenhang = input("Nhập tên hàng: ")
    soluong = int(input("Nhập số lượng: "))
    giaban = int(input("Nhập giá bán: "))
    DS.append(HANGHOA(mahang,tenhang,soluong,giaban))
print("Danh sách các mặt hàng: ")
for i in range(n):
    DS[i].xuat()
f = open("F:\Python\Week 1\hanghoa.txt", "w")
for i in range(n):
    if DS[i].giaban > 20000:
         f.write(DS[i].mahang+";"+DS[i].tenhang+";"+str(DS[i].soluong)+";"+str(DS[i].giaban)+"\n")
f.close()
